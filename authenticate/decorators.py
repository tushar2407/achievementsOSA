from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from authenticate.models import Profile

def is_admin(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/auth/api/profile'):
    '''
    Decorator for views that checks that the logged in user is an admin,
    returns a JsonResponse if not an admin
    '''
    actual_decorator = user_passes_test(
        lambda u: Profile.objects.get(user=u).is_admin(),
        login_url = login_url,
        redirect_field_name = redirect_field_name 
    )
    if function:
        return actual_decorator(function)
    return actual_deocrator(function)