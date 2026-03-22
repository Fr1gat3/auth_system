import bcrypt
import jwt

from datetime import timedelta
from django.utils import timezone
from django.conf import settings

JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = "HS256"
JWT_EXP_MINUTES = 60


def create_access_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": timezone.now() + timedelta(minutes=JWT_EXP_MINUTES),
        "iat": timezone.now(),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_access_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())
