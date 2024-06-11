from django.shortcuts import render
from cart.cart import Cart
from .models import ShippingAddress
from .forms import ShippingForm

# Create your views here.
def paymentSuccess(request):
    return render(request, 'paymentSuccess.html', {})

def checkout(request):
    cart = Cart(request)
    cart_prods = cart.getProd
    quantities = cart.getQuants
    totals = cart.cartTotal()
    if request.user.is_authenticated:
        Sh_user = ShippingAddress.objects.get(user__id=request.user.id)
        Sh_form = ShippingForm(request.POST or None, instance=Sh_user)
        return render(request, 'checkout.html', {'cart_products':cart_prods, 'quantities':quantities, 'total':totals, 'Sh_form':Sh_form})
    else:
        Sh_form = ShippingForm(request.POST or None)
        return render(request, 'checkout.html', {'cart_products':cart_prods, 'quantities':quantities, 'total':totals, 'Sh_form':Sh_form})