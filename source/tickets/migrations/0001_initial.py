# Generated by Django 5.0.4 on 2024-05-09 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OffresTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(blank=True)),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('number_of_place', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (4, 'Four')])),
                ('image', models.ImageField(upload_to='offres_tickets')),
            ],
            options={
                'verbose_name': 'OffresTickets',
                'verbose_name_plural': 'OffresTickets',
            },
        ),
    ]
