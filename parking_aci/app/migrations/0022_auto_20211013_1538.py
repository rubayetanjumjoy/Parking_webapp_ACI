# Generated by Django 3.2.8 on 2021-10-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20211013_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='id',
            field=models.BigAutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='vehicle_number',
            field=models.TextField(max_length=100),
        ),
    ]
