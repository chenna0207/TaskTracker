from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from TaskTrackerApp.models import UserProjectRole

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden()

            # Retrieve the user's roles based on UserProjectRole
            user_roles = UserProjectRole.objects.filter(user=request.user).values_list('role', flat=True)

            # Check if any of the user's roles match the allowed roles
            if any(role in allowed_roles for role in user_roles):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()

        return _wrapped_view

    return decorator
