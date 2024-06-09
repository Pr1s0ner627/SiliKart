from django.shortcuts import render, redirect
from . import models
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm
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
    cat = cat.replace('-', ' ')
    category = models.Categorie.objects.get(CatName=cat)
    products = models.Product.objects.filter(ProdCat=category)
    return render(request, 'category.html', {'products': products, 'category': category})

def categorySummary(request):
    categories = models.Categorie.objects.all()
    return render(request, 'categorySummary.html', {'Categories':categories})

def editUser(request):
    if request.user.is_authenticated:
        currentUser = User.objects.get(id=request.user.id)
        userForm = UpdateUserForm(request.POST or None, instance=currentUser)
        if userForm.is_valid():
            userForm.save()
            login(request, currentUser)
            messages.success(request, "user has been Updated")
            return redirect('home')
        return render(request, 'updateUser.html', {'userForm':userForm})
    else:
        messages.success(request, "You must be Logged in to Access This page")
        return redirect('home')

def editPassword(request):
    if request.user.is_authenticated:
        currentUser = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(currentUser, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Password Changed Successfully...")
                # login(request, currentUser)
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('editPassword')
        else:
            form = ChangePasswordForm(currentUser)
            return render(request, 'editPassword.html', {'form':form})
    else:
        messages.success(request, "You must be Logged In to View that details...")
        return redirect('home')