from django.utils.functional import wraps
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.authtoken.models import Token

from UserManagement.models import Users
from UserManagement.utils import token_expire_handler


def user_role(user_roles):
    """
    we used this previously but now we don't need it.
    user_id = 'not_auth'
    if request.user.is_authenticated:
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_id = request.user.id
            user = Users.objects.get(id=user_id)
            if user.role in user_roles:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapper
    return decorator


def check_token_expiry():
    # check token expiry if it is expire delete the token.
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            token = Token.objects.get(user=request.user)
            if not token_expire_handler(token):
                return view_func(request, *args, **kwargs)
            raise AuthenticationFailed
        return wrapper
    return decorator
