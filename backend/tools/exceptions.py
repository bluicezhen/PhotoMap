from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class LoginFailedException(APIException):
    status_code = 401
    default_detail = _('Incorrect username or password')
    default_code = 'login_failed'
