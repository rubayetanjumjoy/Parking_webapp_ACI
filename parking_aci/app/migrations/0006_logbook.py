# Generated by Django 3.2.8 on 2021-10-10 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_registration_vehicle_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.registration')),
            ],
        ),
    ]
