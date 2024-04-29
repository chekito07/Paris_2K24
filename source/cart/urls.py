from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
    path('update/', views.cart_update, name='cart_update'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('users_info/', views.ticket_user_info, name='users-info'),
    path('card_holder/', views.credit_card_holder_info, name='card-holder'),
    path('user_ticket/', views.display_user_ticket, name='user-ticket'),
]
