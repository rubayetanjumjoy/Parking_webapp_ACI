# Generated by Django 3.2.8 on 2021-10-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_registration_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(choices=[('In', 'In'), ('Out', 'Out')], default='Out', max_length=100),
        ),
    ]