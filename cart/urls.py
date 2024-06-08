from django.urls import path
from . import views

urlpatterns = [
    path('cartSummary/', views.cartSummary ,name='cartSummary'),
    path('cartAdd/', views.cartAdd ,name='cartAdd'),
    path('cartUpdate/', views.cartUpdate ,name='cartUpdate'),
    path('cartDelete/', views.cartDelete ,name='cartDelete'), 
]