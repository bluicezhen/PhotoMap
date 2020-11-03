import json
from typing import TYPE_CHECKING

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sts.sts import Sts

from backend.settings import TENCENT_SECRET_ID, TENCENT_SECRET_KEY, TENCENT_COS_REGION, TENCENT_COS_BUCKET

if TYPE_CHECKING:
    from rest_framework.request import Request


class TencentCOSCredentialsView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request: 'Request', *args, **kwargs):
        """
        https://github.com/tencentyun/qcloud-cos-sts-sdk/blob/master/python/demo/sts_demo.py
        """
        config = {
            'url': 'https://sts.tencentcloudapi.com/',
            'domain': 'sts.tencentcloudapi.com',
            # Valid time
            'duration_seconds': 1800,  # 30min
            'secret_id': TENCENT_SECRET_ID,
            'secret_key': TENCENT_SECRET_KEY,
            'bucket': TENCENT_COS_BUCKET,
            'region': TENCENT_COS_REGION,
            'allow_prefix': 'test.jpg',
            'allow_actions': [
                # Simple Upload
                'name/cos:PutObject',
                'name/cos:PostObject',
            ],
        }

        response = Sts(config).get_credential()
        return Response(response.get('credentials'))
