from rest_framework.serializers import ModelSerializer

from backend.models import PhotoModel


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ['id', 'file_name']
