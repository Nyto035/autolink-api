from rest_framework import serializers

import bina_bikers.delivery_order.models as models


class DeliveryOrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField()
    courier_name = serializers.ReadOnlyField()
    goods_name = serializers.ReadOnlyField(
        source='delivery_good.name')
    goods_description = serializers.ReadOnlyField(
        source='delivery_good.description')

    class Meta:
        model = models.DeliveryOrder
        fields = ('id', 'delivery_good', 'customer', 'courier', 'source',
            'source_name', 'destination', 'destination_name','status',
            'order_time', 'customer_name', 'goods_name', 'goods_description',
            'courier_name')
