# Generated by Django 3.2.8 on 2021-10-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_v_type_registration_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='vehicle_type',
            field=models.TextField(choices=[('car', 'Car'), ('Motor Bike', 'Motor Bike'), ('pickup van', 'Pickup Van')], default=''),
        ),
    ]