from rest_framework.routers import SimpleRouter

import bina_bikers.delivery_good.views as views

router = SimpleRouter()
router.register(r'delivery_goods', views.DeliveryGoodViewSet, 'delivery_goods')

urlpatterns = router.urls
