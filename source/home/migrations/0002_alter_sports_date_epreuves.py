# Generated by Django 5.0.4 on 2024-04-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sports',
            name='date_epreuves',
            field=models.CharField(max_length=250),
        ),
    ]