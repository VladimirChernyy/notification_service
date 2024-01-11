from django.db.models import Count


def get_mailing_statistics(mailing):
    message_status = mailing.objects.values('status').annotate(
        count=Count('status'))
    mailing_data = {
        'mailing_id': mailing.id,
        'start_time': mailing.start_time,
        'end_time': mailing.end_time,
        'message_status': message_status
    }
    return mailing_data
