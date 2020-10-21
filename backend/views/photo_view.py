from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from backend.models import PhotoModel
from backend.serializers import PhotoSerializer


class PhotoView(ListModelMixin, GenericViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    queryset = PhotoModel.objects
    serializer_class = PhotoSerializer
