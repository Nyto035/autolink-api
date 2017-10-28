from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from bina_bikers.geoloc.views import views

router = SimpleRouter()
router.register(r'geloc', views.CourierLocationViewSet, 'geloc')

urlpatterns = router.urls
