from django.utils.functional import wraps
from rest_framework.exceptions import PermissionDenied

from UserManagement.models import Users


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
