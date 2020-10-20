from django.contrib import admin

from backend.models import PhotoModel


@admin.register(PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name')
