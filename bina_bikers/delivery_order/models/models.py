from django.contrib.gis.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from bina_bikers.common.models import AbstractBase
from bina_bikers.user.models import User
from bina_bikers.delivery_good.models import DeliveryGood


ORDERSTATUS = (
    ('ACCEPTED', 'accepted'),
    ('PENDING', 'pending'),
    ('CANCELLED', 'cancelled'),
    ('PAID', 'paid'),
)


class DeliveryOrder(AbstractBase):
    delivery_good = models.ForeignKey(
        DeliveryGood, on_delete=models.PROTECT,
        related_name='delivery_good_delivery_orders')
    customer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='customer_delivery_goods')
    courier = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='courier_delivery_goods',
        null=True, blank=True)
    source = models.PointField()
    source_name = models.CharField(_('source_name'), max_length=255)
    destination = models.PointField()
    destination_name = models.CharField(_('destination_name'), max_length=255)
    status = models.CharField(
        max_length=50, choices=ORDERSTATUS, default='PENDING')
    order_time = models.DateTimeField(default=timezone.now)
    distance = models.FloatField()
    total_cost = models.FloatField()

    _search_fields = (
        'customer.first_name', 'customer.last_name', 'courier.first_name',
        'courier.last_name', 'source_name', 'destination_name', 'status')

    def __str__(self):
        return '{} {}'.format(self.customer.first_name, self.delivery_good.name)

    @property
    def customer_name(self):
        return '{} {}'.format(
            self.customer.first_name, self.customer.last_name)

    @property
    def courier_name(self):
        if self.courier:
            return '{} {}'.format(
                self.courier.first_name, self.courier.last_name)
        return None
