from rest_framework.routers import SimpleRouter

import bina_bikers.websocket.views as views

router = SimpleRouter()
router.register(r'users', views.UserViewSet, 'users')
router.register(r'userprofiles', views.UserProfileViewSet, 'userprofiles')

urlpatterns = router.urls
