import django_filters

import bina_bikers.geoloc.models as models
from bina_bikers.common.filters import BaseFilterSet


class CurrentCourierLocationFilter(BaseFilterSet):
    courier = django_filters.CharFilter(name='courier')
    latest_couriers = django_filters.BooleanFilter(method='get_latest_couriers')

    def get_latest_couriers(self, queryset, field, value):
        if value:
            return queryset.filter(time_interval__lte=15)
        return queryset.filter(time_interval__gte=15)

    class Meta:
        model = models.CurrentCourierLocation
        fields = ('courier', 'time_interval',)
