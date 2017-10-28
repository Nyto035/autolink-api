from __future__ import division

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.db import transaction
from rest_framework.response import Response

from rest_framework.decorators import list_route
# import bina_bikers.delivery_good.filters as filters
import bina_bikers.delivery_good.serializers as serializers
import bina_bikers.delivery_good.models as models
from bina_bikers.delivery_order.models import  DeliveryOrder
from django.contrib.gis.geos import Point


class DeliveryGoodViewSet(ModelViewSet):
    """
    This is the deliver goods endpoint. It contains the details that are stored for
    goods using our system.
    """
    queryset = models.DeliveryGood.objects.all()
    # filter_class = filters.DeliveryGoodFilter
    serializer_class = serializers.DeliveryGoodSerializer
    search_fields = ('name', 'description',)

    @transaction.atomic()
    @list_route(methods=['post'])
    def make_delivery_order(self, request, *args, **kwargs):
        """
        Make an deliver order

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = {
            'owner': request.user,
            'name': request.data['name'],
            'description': request.data['description'],
        }
        delivery_goods = models.DeliveryGood.objects.create(**data)

        estimate_distance = request.data['distance'] / 1000
        if estimate_distance < 1:
            estimate_cost = 50
        else:
            estimate_cost = (estimate_distance * 20) + 50


        delivery_order = {
            'delivery_good': delivery_goods,
            'customer': request.user,
            'source': Point(source[0], source[1]),
            'source_name':  request.data['source_name'],
            'destination': Point(destination[0], destination[1]),
            'destination_name':request.data['destination_name'],
            'distance': request.data['distance'],
            'total_cost': estimate_cost,
        }
        delivery_order = DeliveryOrder(**delivery_order)
        delivery_order.save()
        return Response(
            self.serializer_class(delivery_goods).data, status=201)
