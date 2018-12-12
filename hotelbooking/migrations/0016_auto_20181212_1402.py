# Generated by Django 2.0 on 2018-12-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0015_auto_20181212_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliable_room_no', models.IntegerField()),
                ('select_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='reserve_room',
            name='room_type',
        ),
        migrations.RemoveField(
            model_name='display',
            name='room_no',
        ),
        migrations.RemoveField(
            model_name='room',
            name='avaliable_rooms',
        ),
        migrations.AddField(
            model_name='room',
            name='max_numbers',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='total_rooms',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Reserve_Room',
        ),
    ]