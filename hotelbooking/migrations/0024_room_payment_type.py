# Generated by Django 2.0 on 2018-12-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0023_room_available_roomno'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='payment_type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]