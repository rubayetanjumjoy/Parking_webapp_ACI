# Generated by Django 3.2.8 on 2021-10-10 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_registration_v_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='v_type',
            new_name='vehicle_type',
        ),
    ]
