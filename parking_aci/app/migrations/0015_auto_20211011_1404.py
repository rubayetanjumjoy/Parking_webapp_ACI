# Generated by Django 3.2.8 on 2021-10-11 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20211011_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='entry',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='exit',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.registration'),
        ),
    ]
