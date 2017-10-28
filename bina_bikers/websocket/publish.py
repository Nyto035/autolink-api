from channels.binding.websockets import WebsocketBinding

from bina_bikers.delivery_order.serializers import DeliveryOrderSerializer
from bina_bikers.geoloc.serializers import CurrentCourierLocationSerializer

from django.conf import settings
from channels.binding.websockets import WebsocketBinding



class DelieryOrderPublisher(WebsocketBinding):
    model = 'delivery_order.DeliveryOrder'

    stream = 'delivery'

    fields = ['__all__']

    def serialize(self, instance, action):
        data = DeliveryOrderSerializer(instance).data
        data['push_action'] = action
        return data

    @classmethod
    def group_names(cls, instance):
        return ['delivery']

    def send_messages(self, instance, group_names, action, **kwargs):
        return super(
            DelieryOrderPublisher,
            self).send_messages(instance, group_names, action, **kwargs)


class CourierLocationPublisher(WebsocketBinding):
    model = 'geoloc.CurrentCourierLocation'

    stream = 'geoloc'

    fields = ['__all__']

    def serialize(self, instance, action):
        data = CurrentCourierLocationSerializer(instance).data
        data['push_action'] = action
        return data

    @classmethod
    def group_names(cls, instance):
        return ['geoloc']

    def send_messages(self, instance, group_names, action, **kwargs):
        return super(
            CourierLocationPublisher,
            self).send_messages(instance, group_names, action, **kwargs)
