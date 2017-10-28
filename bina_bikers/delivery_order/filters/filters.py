import django_filters

import bina_bikers.delivery_order.models as models
from bina_bikers.common.filters import BaseFilterSet


class DeliveryOrderFilter(BaseFilterSet):
    customer = django_filters.CharFilter(name='customer')
    courier = django_filters.CharFilter(name='courier')

    class Meta:
        model = models.DeliveryOrder
        fields = ('status', 'customer', 'courier',)
