import urllib.parse
from urllib.parse import urlparse
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
from .config import CLIENT_URL


User = get_user_model()


def get_client_url(user: User):
    refresh = RefreshToken.for_user(user)
    params = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return f'{CLIENT_URL}?{urllib.parse.urlencode(params)}'
