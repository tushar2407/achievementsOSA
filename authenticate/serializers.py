from django.contrib.auth.models import User
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers, exceptions
from achievements import settings
from django.utils.translation import ugettext_lazy as _
from allauth.account.utils import send_email_confirmation, perform_login
from django.contrib.auth import get_user_model, authenticate

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
        
        print(username)
        print(email)
        print(password)

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
