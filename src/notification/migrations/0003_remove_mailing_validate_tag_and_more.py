# Generated by Django 5.0.1 on 2024-01-14 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_alter_client_operator_code_alter_client_tag_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='mailing',
            name='validate_tag',
        ),
        migrations.RemoveConstraint(
            model_name='mailing',
            name='validate_operator_code',
        ),
    ]
