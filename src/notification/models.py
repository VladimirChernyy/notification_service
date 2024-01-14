import pytz

from django.db import models

from .validators import phone_number_validator, operator_code_validator


class StatusChoices(models.TextChoices):
    SENT = 'Sent', 'Отправлено'
    REJECTED = 'Rejected', 'Не доставлено'


class OperatorTagAbstractModel(models.Model):
    operator_code = models.CharField(
        'Код оператора',
        max_length=3,
        validators=[operator_code_validator]
    )
    tag = models.CharField(
        'Ter',
        max_length=150
    )

    class Meta:
        abstract = True


class Mailing(OperatorTagAbstractModel, models.Model):
    start_time = models.DateTimeField('Время начала рассылки')
    end_time = models.DateTimeField('Время окончания рассылки')
    text = models.TextField('Текст сообщения')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_time__lte=models.F('end_time')),
                name='validate_start_time',
                violation_error_message='Время начала рассылки не может быть '
                                        'позднее окончания',
            ),
            # models.CheckConstraint(
            #     check=~models.Q(tag__isnull=True),
            #     name='validate_tag',
            #     violation_error_message='Данного тега не существует'
            # ),
            # models.CheckConstraint(
            #     check=~models.Q(operator_code__isnull=True),
            #     name='validate_operator_code',
            #     violation_error_message='Данного кода оператора не существует'
            # )
        ]

    def __str__(self):
        return f'id({self.id}) {self.start_time}'


class Client(OperatorTagAbstractModel, models.Model):
    TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]

    phone_number = models.CharField(
        'Номер телефона',
        max_length=11,
        validators=[phone_number_validator]
    )
    time_zone = models.CharField(
        'Часовой пояс',
        choices=TIMEZONE_CHOICES,
        max_length=255,
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'id({self.id}) {self.phone_number}'

    def save(self, *args, **kwargs):
        self.operator_code = str(self.phone_number)[1:4]
        return super(Client, self).save(*args, **kwargs)


class Message(models.Model):
    created_at = models.DateTimeField(
        'Дата создания сообщения',
        auto_now_add=True
    )
    status = models.CharField(
        'Статус сообщения',
        choices=StatusChoices.choices
    )

    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.SET_NULL,
        null=True,
        related_name='mailing',
        verbose_name='Рассылка'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True, related_name='client',
        verbose_name='Клиент'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.created_at} {self.status}'
