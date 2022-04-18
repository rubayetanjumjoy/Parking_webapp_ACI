# Generated by Django 3.2.8 on 2021-10-10 09:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_logbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('ts_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.registration')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('ts_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.registration')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]