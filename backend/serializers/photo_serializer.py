from typing import TYPE_CHECKING

from rest_framework.serializers import ModelSerializer

from backend.models import PhotoModel

if TYPE_CHECKING:
    from rest_framework.request import Request


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ['id', 'file_name', 'file_size']

    def create(self, validated_data):
        request: 'Request' = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
