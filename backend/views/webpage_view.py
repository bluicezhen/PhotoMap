import requests
from django.http.response import HttpResponse
from rest_framework.views import APIView
from requests.exceptions import ConnectionError


class WebpageView(APIView):

    @staticmethod
    def get(request):
        url = 'http://localhost:8001' + request.path

        try:
            res = requests.get(url)
            return HttpResponse(res.content, content_type=res.headers.get('content-type'))
        except ConnectionError:
            return HttpResponse("Pleases run 'yarn run serve'")

