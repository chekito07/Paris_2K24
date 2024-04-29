from django.db import models
from django.utils.text import slugify


# Create your models here.
class Sports(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    site = models.TextField()
    sport_date = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image_sport/")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
