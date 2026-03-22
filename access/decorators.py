from rest_framework.response import Response
from rest_framework import status
from functools import wraps
from access.services import has_permission
from users.models import User as AccountUser


def require_permission(element, action):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):

            user = getattr(request, "user", None)

            if not isinstance(user, AccountUser):
                return Response(
                    {"detail": "Authentication required"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            if not has_permission(user, element, action):
                return Response(
                    {"detail": "Forbidden"},
                    status=status.HTTP_403_FORBIDDEN,
                )

            return view_func(self, request, *args, **kwargs)

        return wrapper

    return decorator
