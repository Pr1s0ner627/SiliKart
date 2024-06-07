from django.shortcuts import render, redirect
from . import models
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.
def home(request):
    products = models.Product.objects.all()
    return render(request, 'index.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def product(request, pk):
    product = models.Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in..."))
            return redirect('home')
        else:
            messages.success(request, ("Email or Password do not match."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return redirect('home')

def registerUser(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered successfully!!!"))
            return redirect('home')
        else:
            messages.success(request, ("Please fill all details..."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})

def category(request, cat):
    cat = cat.replace('-',' ')
    try:
        category = models.Categorie.objects.get(name=cat)
        products = models.Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category}) 
    except:
        return redirect('home')