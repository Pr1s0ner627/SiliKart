from django.urls import path
from . import views

urlpatterns = [
    path('paymentSuccess/', views.paymentSuccess ,name='paymentSuccess'),
    path('checkout/', views.checkout, name='checkout')
]