from django.utils.deprecation import MiddlewareMixin
from .utils import decode_access_token
from .models import User


class JWTAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = None

        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return

        if not auth_header.startswith("Bearer "):
            return

        token = auth_header.split(" ")[1]
        payload = decode_access_token(token)
        if not payload:
            return

        try:
            user = User.objects.get(id=payload["user_id"], is_active=True)
            request.user = user
        except User.DoesNotExist:
            return
