import re

from django.core.exceptions import ValidationError


def phone_number_validator(value):
    regex = re.compile(r'^7\d{10}$')
    if not regex.match(value):
        raise ValidationError('Номер телефона должен быть формата 7XXXXXXXXXX')


def operator_code_validator(value):
    regex = re.compile(r'^\d{1,3}$')
    if not regex.match(value):
        raise ValidationError('Введите 3 цифры вашего оператора')
