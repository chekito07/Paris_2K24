from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sport/<slug:slug>', views.details_sport, name="sport"),
]
