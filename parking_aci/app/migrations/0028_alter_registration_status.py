# Generated by Django 3.2.8 on 2021-10-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_logbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(default='Out', max_length=100),
        ),
    ]