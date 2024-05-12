from django.contrib import admin
from .models import OffresTickets

# Register your models here.
@admin.register(OffresTickets)
class OffresTicketsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'number_of_place']

