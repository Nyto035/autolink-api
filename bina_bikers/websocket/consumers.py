import json

from channels import Group
from channels.generic.websockets import WebsocketDemultiplexer
from channels.sessions import channel_session
from bina_bikers.websocket.publish import (
    DelieryOrderPublisher, CourierLocationPublisher, )


class ConsumerDemultiplexer(WebsocketDemultiplexer):
    consumers = {
        "delivery": DelieryOrderPublisher.consumer,
    }

    def connection_groups(self):
        return ["delivery"]

class CourierConsumerDemultiplexer(WebsocketDemultiplexer):
    consumers = {
        "geoloc": CourierLocationPublisher.consumer,
    }

    def connection_groups(self):
        return ["geoloc"]
