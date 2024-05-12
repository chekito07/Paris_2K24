from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Sports(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    site = models.TextField()
    sport_date = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image_sport/")

    class Meta:
        verbose_name = 'Sports'
        verbose_name_plural = 'Sports'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('sport', kwargs={'slug': self.slug})
