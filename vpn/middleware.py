import requests
from rest_framework.exceptions import AuthenticationFailed

SSO_VALIDATE_URL = "http://127.0.0.1:8003/akses/sso/validate/"
SSO_LOGOUT_URL = "http://127.0.0.1:8003/akses/sso/logout/"

class JWTSSOMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            response = requests.post(SSO_VALIDATE_URL, json={'token': token})
            if response.status_code != 200:
                raise AuthenticationFailed("token invalid atau expired.")
        return self.get_response(request)