from django.contrib.auth.models import User
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers, exceptions
from achievements import settings
from django.utils.translation import ugettext_lazy as _
from allauth.account.utils import send_email_confirmation, perform_login
from django.contrib.auth import get_user_model, authenticate

from authenticate.models import Profile

class UserLoginSerializer(LoginSerializer):
    # password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_username_email(self, username, email, password):
        user = None

        if username and password:
            try:
                user = self.authenticate(username=username, password=password)
            except:
                pass
        elif email and password:
            try:
                user = self.authenticate(username=User.objects.get(email = email).username, password=password)
            except:
                pass
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        
        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            user = self._validate_username_email(username, email, password)

        else:
            # Authentication without using allauth
            if email:
                try:
                    username = User.objects.get(email__iexact=email).get_username()
                except User.DoesNotExist:
                    pass

            if username:
                user = self._validate_username_email(username, '', password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            print(user)
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    perform_login(self.context['request'], user, app_settings.EMAIL_VERIFICATION)
                    raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs

class ProfileSerializer(serializers.ModelSerializer):
    profile_pic = serializers.FileField(required = False)
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False},
            'address':{'required':False},
            'group':{'required':False},
            'skills':{'required':False},
            'facebook':{'required':False},
            'instagram':{'required':False},
            'twitter':{'required':False},
            'github':{'required':False},
        }
    
    def create(self, validated_data):
        request = self.context.get("request")
        instance = super().create(validated_data)
        files = request.FILES
        if files:
            for f in files.getlist("files"):
                instance.profile_pic.create(file=f)
        return instance
    
    def update(self, instance, validated_data):
        request = self.context.get("request")
        _ = super().update(instance, validated_data)
                
        files = request.FILES
        if files:
            instance.profile_pic.delete()
            for f in files.getlist("profile_pic"):
                instance.profile_pic.save(name=f.name, content=f)
        
        return instance
