# Generated by Django 3.2.9 on 2021-11-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20211115_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name_plural': 'History'},
        ),
        migrations.AddField(
            model_name='history',
            name='status',
            field=models.CharField(choices=[('In', 'In'), ('Out', 'Out')], default='', max_length=100),
        ),
    ]