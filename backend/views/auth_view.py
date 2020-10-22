from typing import TYPE_CHECKING

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.serializers import AuthSerializer
from backend.tools.exceptions import LoginFailedException

if TYPE_CHECKING:
    from rest_framework.request import Request


class AuthView(APIView):
    @staticmethod
    def post(request: 'Request', *args, **kwargs):
        """Login
        For Test: {"username":"admin", "password":"7777"}
        """
        auth_serializer = AuthSerializer(data=request.data)
        auth_serializer.is_valid(raise_exception=True)
        request_data = auth_serializer.validated_data

        user = authenticate(username=request_data['username'], password=request_data['password'])
        if user is not None:
            login(request, user)
            return Response('ok')
        else:
            raise LoginFailedException()
