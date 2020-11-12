from django.db.models import BooleanField, CharField, CASCADE, ForeignKey, IntegerField, Model
from django.contrib.auth.models import User


class PhotoModel(Model):
    file_name = CharField(max_length=256, null=False)
    file_size = IntegerField()
    user = ForeignKey(User, on_delete=CASCADE)
    is_upload_tencent_cos = BooleanField(default=False)
