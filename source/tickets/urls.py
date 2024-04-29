from django.urls import path
from . import views

urlpatterns = [
    path('billet/', views.billetterie, name="billet"),
    path('billet/details/<slug:slug>', views.details_billet, name="details-billet"),
]
