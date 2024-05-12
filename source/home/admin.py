from django.contrib import admin
from .models import Sports
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display = ['name', 'site', 'sport_date']


admin.site.site_header = _("Paris 2K24")
