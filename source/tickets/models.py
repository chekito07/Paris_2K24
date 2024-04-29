from django.db import models
from django.utils.text import slugify


# Create your models here.
class OffresTickets(models.Model):
    class NumberOfPlace(models.IntegerChoices):
        ONE = 1
        TWO = 2
        FOUR = 4

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(blank=True)
    price = models.DecimalField(default=0, decimal_places=3, max_digits=6)
    number_of_place = models.IntegerField(choices=NumberOfPlace)
    image = models.ImageField(upload_to='offres_tickets')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)