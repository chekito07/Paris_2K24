from django.contrib import admin
from .models import Sports

# Register your models here.
@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display = ['name', 'site', 'sport_date']

