from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.db import transaction
from rest_framework.response import Response

from rest_framework.decorators import detail_route

import bina_bikers.delivery_order.filters as filters
import bina_bikers.delivery_order.serializers as serializers
import bina_bikers.delivery_order.models as models


class DeliveryOrderViewSet(ModelViewSet):
    """
    This is the deliver order endpoint. It contains the details of orders made
    by a customer to deliver cuoriers
    """
    queryset = models.DeliveryOrder.objects.all()
    filter_class = filters.DeliveryOrderFilter
    serializer_class = serializers.DeliveryOrderSerializer
    search_fields = ('name', 'description',)

    @transaction.atomic()
    @detail_route(methods=['patch', 'get'])
    def transition_delivery_order(self, request, pk):
        """
        Make an deliver order

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        courier = request.user
        status = request.data['status']
        delivery_order = models.DeliveryOrder.objects.get(id=str(pk))
        delivery_order.courier = courier
        delivery_order.status = status
        delivery_order.save()
        return Response(
            self.serializer_class(delivery_order).data, status=201)
