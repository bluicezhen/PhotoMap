from django.db.models import CharField, Model


class PhotoModel(Model):
    file_name = CharField(max_length=256, null=False)
