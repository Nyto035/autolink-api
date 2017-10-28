"""bina_bikers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from bina_bikers.user.views import MeView
from bina_bikers.common.views import serve_media

apipatterns = [
    url(r'^user/', include('bina_bikers.user.urls', namespace='user')),
    url(
        r'^delivery_good/', include(
            'bina_bikers.delivery_good.urls', namespace='delivery_good')),
    url(
        r'^delivery_order/', include(
            'bina_bikers.delivery_order.urls', namespace='delivery_order')),

    url(
        r'^geoloc/', include(
            'bina_bikers.geoloc.urls', namespace='geoloc')),
]

authpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token, name='get-token'),
    url(r'^api-token-refresh/', refresh_jwt_token, name='refresh-token'),
]

urlpatterns = [
    url(r'^v1/', include(apipatterns, namespace='api')),
    url(r'^accounts/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/',
        include(authpatterns, namespace='jwt_provider')),
    url(r'^me/$', MeView.as_view(), name='me'),
    url(r'^static/(?P<path>.*)$',
        serve, {'document_root': settings.STATIC_ROOT}),
    url('', include('social_django.urls', namespace='social')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^media\/(?P<path>.*)$', serve_media, name='serve_media'),
]
