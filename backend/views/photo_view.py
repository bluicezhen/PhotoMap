from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from backend.models import PhotoModel
from backend.serializers import PhotoSerializer


class PhotoView(ListModelMixin, GenericViewSet):
    queryset = PhotoModel.objects
    serializer_class = PhotoSerializer
