# Generated by Django 2.0 on 2018-12-12 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0020_room_payment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='available_roomNo',
        ),
        migrations.RemoveField(
            model_name='room',
            name='payment_type',
        ),
    ]
