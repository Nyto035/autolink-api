from json import dumps
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels import Group
from bina_bikers.delivery_order.models import DeliveryOrder


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("order_delivery").add(message.reply_channel)

def send_notification(delivery_notification):
    Group("order_delivery").send({'text': dumps(delivery_notification)})

def ws_message(message):
    delivery_order = message.content['id']
    DeliveryOrder.objects.filter(
        id=delivery_order).update(
            courier= message.content['user'],
            status='ACCEPTED')
    Group("order_delivery").send()

def ws_disconnect(message):
    Group("order_delivery").discard(message.reply_channel)

@receiver(post_save, sender=DeliveryOrder)
def delivery_on_save(sender, instance, **kwargs):
    send_notification({
        "id": str(instance.id),
        "customer": instance.customer.full_name,
        "source": instance.source.geojson,
        "source_name": instance.source_name,
        "destination": instance.destination.geojson,
        "destination_name": instance.destination_name,
        "status": instance.status,
        "order_time": str(instance.order_time)
    })
