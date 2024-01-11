import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from dotenv import load_dotenv

from .models import Mailing, Message

load_dotenv()

TOKEN = os.getenv('JWT_TOKEN')
URL = os.getenv('URL')


@receiver(post_save, sender=Mailing, dispatch_uid='send_message')
def send_message(sender, instance, created, **kwargs):
    pass
