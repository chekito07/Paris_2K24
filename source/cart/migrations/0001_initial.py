# Generated by Django 5.0.4 on 2024-05-09 22:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCardHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(max_length=100)),
                ('card_number', models.DecimalField(decimal_places=0, max_digits=16)),
                ('card_validation_code', models.DecimalField(decimal_places=0, max_digits=3)),
                ('card_validity', models.DateField()),
                ('bought', models.BooleanField(default=True)),
                ('buying_date', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Duo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('cart', models.TextField(blank=True)),
                ('buying_date', models.DateTimeField(auto_now=True, null=True)),
                ('qr_code', models.ImageField(upload_to='qr_codes')),
                ('sport_choice', models.CharField(blank=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('cart', models.TextField(blank=True)),
                ('buying_date', models.DateTimeField(auto_now=True, null=True)),
                ('qr_code', models.ImageField(upload_to='qr_codes')),
                ('sport_choice', models.CharField(blank=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Solo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('cart', models.TextField(blank=True)),
                ('buying_date', models.DateTimeField(auto_now=True, null=True)),
                ('qr_code', models.ImageField(upload_to='qr_codes')),
                ('sport_choice', models.CharField(blank=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
