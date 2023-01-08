from django.conf import settings
from django.urls import include, path
from rest_framework import routers

from .views import SwapiViewSet

router = routers.DefaultRouter()
router.register(r'swapi', SwapiViewSet)

urlpatterns = []

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns