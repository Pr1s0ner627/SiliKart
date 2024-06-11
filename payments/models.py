from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Sh_fullName = models.CharField(max_length=255)
    Sh_email = models.CharField(max_length=255)
    Sh_address1 = models.CharField(max_length=255)
    Sh_address2 = models.CharField(max_length=255, null=True)
    Sh_city = models.CharField(max_length=255)
    Sh_state = models.CharField(max_length=255, null=True, blank=True)
    Sh_zipCode = models.CharField(max_length=255, null=True, blank=True)
    Sh_country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Shipping Address"
    
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    FullName = models.CharField(max_length=150)
    ShippingAddress = models.CharField(max_length=1500)
    Email = models.EmailField()
    AmountPaid = models.DecimalField(decimal_places=2, max_digits=6)
    DateOrdered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self) -> str:
        return f'Order Item - {str(self.id)}'