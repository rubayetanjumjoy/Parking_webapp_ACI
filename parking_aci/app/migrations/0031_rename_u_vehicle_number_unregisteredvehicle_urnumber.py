# Generated by Django 3.2.8 on 2021-10-19 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_unregisteredvehicle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unregisteredvehicle',
            old_name='u_vehicle_number',
            new_name='urnumber',
        ),
    ]
