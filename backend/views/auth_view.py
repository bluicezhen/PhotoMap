from django.contrib.auth.models import User
from rest_framework.views import APIView

from backend.tools import HTTPException
from backend.tools.exceptions import LoginFailedException


class AuthView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        """Login

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        username: str = request.data.get('username')
        password: str = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise LoginFailedException()

        if user.check_password(password):
            return 'ok'

        raise LoginFailedException()
