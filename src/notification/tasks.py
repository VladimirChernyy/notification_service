import os
import requests

from celery import shared_task
from dotenv import load_dotenv

from .models import Message, StatusChoices


load_dotenv()

TOKEN = os.getenv('JWT_TOKEN')
URL = os.getenv('API_URL')
COUNTDOWN = 300


@shared_task(bind=True, max_retries=5)
def send_message_task(
        self, mailing_id, mailing_text,
        client_id, client_phone, time
):
    message = Message.objects.create(
        created_at=time,
        mailing_id=mailing_id,
        client_id=client_id,
        status=StatusChoices.REJECTED
    )
    headers = {'Authorization': f'Bearer {TOKEN}'}
    data = {
        'id': message.id,
        'phone': client_phone,
        'text': mailing_text,
    }
    try:
        response = requests.post(
            url=URL + str(message.id) + '/', headers=headers, json=data
        )
        response.raise_for_status()
        message.status = StatusChoices.SENT
        message.save(update_fields=['status'])
    except requests.exceptions.HTTPError as errh:
        self.retry(exc=errh, countdown=COUNTDOWN)
        print(f"HTTP Error: {errh}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        self.retry(exc=errt, countdown=COUNTDOWN)
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        self.retry(exc=errc, countdown=COUNTDOWN)
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        self.retry(exc=err, countdown=COUNTDOWN)
