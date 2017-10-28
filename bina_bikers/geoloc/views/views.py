from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.db import transaction
from rest_framework.response import Response

from rest_framework.decorators import detail_route

import bina_bikers.geoloc.filters as filters
import bina_bikers.geoloc.serializers as serializers
import bina_bikers.geoloc.models as models


class CourierLocationViewSet(ModelViewSet):
    """
    """
    queryset = models.CurrentCourierLocation.objects.all()
    filter_class = filters.CurrentCourierLocationFilter
    serializer_class = serializers.CurrentCourierLocationSerializer
    search_fields = ()
