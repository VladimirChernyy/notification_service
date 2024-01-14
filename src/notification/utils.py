from django.db.models import Count

from .models import Mailing


def get_mailing_statistics(mailing):
    message_status = mailing.mailing.values('status').annotate(
        count=Count('status'))
    mailing_data = {
        'mailing_id': mailing.id,
        'start_time': mailing.start_time,
        'end_time': mailing.end_time,
        'message_status': message_status
    }
    return mailing_data
