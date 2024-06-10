from django.urls import path
from . import views

urlpatterns = [
    path('paymentSuccess/', views.paymentSuccess ,name='paymentSuccess'),
]