from django.urls import path
from . import views

urlpatterns = [
    path('cartSummary/', views.cartSummary ,name='cartSummary'),
    path('cartAdd/', views.cartAdd ,name='cartAdd'),
    path('cartUpdate/', views.cartDelete ,name='cartDelete'),
    path('cartDelete/', views.cartUpdate ,name='cartUpdate') 
]