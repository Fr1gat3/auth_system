from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from users.utils import decode_access_token
from users.models import User


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        if not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]
        payload = decode_access_token(token)

        if not payload:
            raise AuthenticationFailed("Invalid or expired token")

        try:
            user = User.objects.get(
                id=payload["user_id"],
                is_active=True
            )
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")

        return (user, None)