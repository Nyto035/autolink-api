from rest_framework.routers import SimpleRouter

import bina_bikers.delivery_order.views as views

router = SimpleRouter()
router.register(r'delivery_orders', views.DeliveryOrderViewSet, 'delivery_orders')

urlpatterns = router.urls
