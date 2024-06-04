from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    products = models.Product.objects.all()
    return render(request, 'index.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})
