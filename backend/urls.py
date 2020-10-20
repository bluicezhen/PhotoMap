from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backend.views import PhotoView

router = DefaultRouter()
router.register(r'photo', PhotoView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
