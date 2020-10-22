from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from backend.settings import DEBUG
from backend.views import AuthView, PhotoView, WebpageView

router = DefaultRouter()
router.register(r'photo', PhotoView)

urlpatterns = [
    url('^api/auth/', AuthView.as_view()),
    url('^api/', include(router.urls)),
    url('^admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns.append(url('^', WebpageView.as_view()))
