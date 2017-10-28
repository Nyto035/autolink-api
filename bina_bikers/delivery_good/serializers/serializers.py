from rest_framework import serializers

import bina_bikers.delivery_good.models as models


class DeliveryGoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DeliveryGood
        fields = (
            'id', 'owner', 'name', 'description',)
