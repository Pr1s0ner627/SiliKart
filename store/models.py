from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateModified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=500, blank=True)
    address2 = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    state = models.CharField(max_length=500, blank=True)
    zipCode = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=500, blank=True)
    old_cart = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

def createProfile(sender, instance, created, **kwargs):
    if created:
        userProfile = Profile(user=instance)
        userProfile.save()

post_save.connect(createProfile, sender=User)

# Category of Product
class Categorie(models.Model):
    CatName = models.CharField(max_length=50)
    def __str__(self):
        return self.CatName
    
# Customer Data    
class Customer(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.CharField(max_length=10)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.FirstName} {self.LastName}'

# Product Details
class Product(models.Model):
    ProdName = models.CharField(max_length=50)
    ProdPrice = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    ProdCat = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    ProdDesc = models.CharField(max_length=500)
    ProdImage = models.ImageField(upload_to='uploads/product/')
    ProdOnSale = models.BooleanField(default=False)
    ProdSalePrice = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.ProdName

# Customer Order Records
class Order(models.Model):
    OrderProd = models.ForeignKey(Product, on_delete=models.CASCADE)
    OrderUser = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderQuant = models.IntegerField(default=1)
    OrderAddress = models.CharField(max_length=200)
    OrderPhone = models.CharField(max_length=20)
    OrderTime = models.DateTimeField(default=datetime.datetime.now)
    OrderStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.OrderProd

