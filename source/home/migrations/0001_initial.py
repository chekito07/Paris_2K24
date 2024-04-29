# Generated by Django 5.0.4 on 2024-04-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('site', models.CharField(max_length=60)),
                ('date_epreuves', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='image_sport/')),
            ],
        ),
    ]