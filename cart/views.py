from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store import models
from django.http import JsonResponse
# Create your views here.
def cartSummary(request):
    cart = Cart(request)
    cart_prods = cart.getProd
    quantities = cart.getQuants
    return render(request, 'cartSummary.html', {'cart_products':cart_prods, 'quantities':quantities})

def cartAdd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(models.Product, id=product_id)
    cart.add(product=product, quantity=product_qty)
    cart_quantity = cart.__len__()
    # response = JsonResponse({'Name':product.ProdName})
    # return response
    response = JsonResponse({'Quantity':cart_quantity})
    return response

def cartUpdate(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        
        response = JsonResponse({'Quantity':product_qty})
    return response

def cartDelete(request):
    pass