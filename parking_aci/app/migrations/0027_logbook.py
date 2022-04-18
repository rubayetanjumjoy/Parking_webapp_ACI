# Generated by Django 3.2.8 on 2021-10-18 10:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_registration_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='logbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('ts_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.CharField(choices=[('In', 'In'), ('Out', 'Out')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.registration')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
