import pytz

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Mailing, Client
from .tasks import send_message_task


@receiver(post_save, sender=Mailing, dispatch_uid='create_mailing')
def create_mailing(sender, instance, created, **kwargs):
    if created:
        current_time = timezone.now()
        mailing = Mailing.objects.get(pk=instance.id)
        clients = Client.objects.filter(
            operator_code=mailing.operator_code, tag=mailing.tag
        )
        for client in clients:
            client_timezone = pytz.timezone(client.time_zone)
            start_time_client_tz = mailing.start_time.astimezone(client_timezone)
            end_time_client_tz = mailing.end_time.astimezone(client_timezone)
            if start_time_client_tz > current_time:
                delay = (start_time_client_tz - current_time).total_seconds()
                send_message_task.apply_async(
                    args=[
                        mailing.id,
                        mailing.text,
                        client.id,
                        client.phone_number,
                        current_time
                    ],
                    countdown=delay,
                )

            if start_time_client_tz < current_time <= end_time_client_tz:
                send_message_task.delay(
                        mailing.id,
                        mailing.text,
                        client.id,
                        client.phone_number,
                        current_time,
                )
