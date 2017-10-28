from channels.routing import route, route_class

from bina_bikers.websocket.consumers import(
    ConsumerDemultiplexer, CourierConsumerDemultiplexer)
from bina_bikers.websocket.publish import (
    DelieryOrderPublisher, CourierLocationPublisher)

channel_routing = [
    route_class(ConsumerDemultiplexer, path='^/delivery/?$'),
    route('delivery', DelieryOrderPublisher.consumer),

    route_class(CourierConsumerDemultiplexer, path='^/geoloc/?$'),
    route('geoloc', CourierLocationPublisher.consumer),
]
