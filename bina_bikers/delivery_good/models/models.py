from django.contrib.gis.db import models

from django.utils.translation import gettext_lazy as _

from bina_bikers.common.models import AbstractBase
from bina_bikers.user.models import User



class DeliveryGood(AbstractBase):
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_delivery_goods')
    name = models.CharField(_('name'), max_length=30)
    description = models.TextField()

    _search_fields = (
        'owner.first_name', 'owner.last_name', 'name', 'description')

    def __str__(self):
        return self.name
