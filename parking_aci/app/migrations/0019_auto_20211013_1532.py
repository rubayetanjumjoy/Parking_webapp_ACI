# Generated by Django 3.2.8 on 2021-10-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_registration_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='id',
        ),
        migrations.AlterField(
            model_name='registration',
            name='vehicle_number',
            field=models.TextField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
