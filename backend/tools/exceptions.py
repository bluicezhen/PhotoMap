from rest_framework.exceptions import APIException


class LoginFailedException(APIException):
    status_code = 403
    default_detail = 'Incorrect username or password'
    default_code = 'login_failed'
