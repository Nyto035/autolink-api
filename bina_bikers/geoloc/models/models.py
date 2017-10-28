from django.contrib.gis.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from bina_bikers.common.models import AbstractBase
from bina_bikers.user.models import User


class CurrentCourierLocation(AbstractBase):
    courier = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='courier_current_location',)
    current_location = models.PointField(null=True, blank=True)
    time_interval = models.FloatField(null=True, blank=True)
    location_time = models.DateTimeField(default=timezone.now)

    _search_fields = (
        'courier.first_name', 'courier.last_name',)

    def __str__(self):
        return '{} {}'.format(self.customer.first_name, "Location")

    @property
    def courier_name(self):
        if self.courier:
            return '{} {}'.format(
                self.courier.first_name, self.courier.last_name)
        return None
