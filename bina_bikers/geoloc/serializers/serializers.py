from rest_framework import serializers

import bina_bikers.geoloc.models as models

class CurrentCourierLocationSerializer(serializers.ModelSerializer):
    courier_name = serializers.ReadOnlyField()

    class Meta:
        model = models.CurrentCourierLocation
        fields = (
            'id', 'courier', 'current_location', 'location_time',
            'courier_name', 'location_time', 'time_interval')
