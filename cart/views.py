from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store import models
from django.http import JsonResponse
# Create your views here.
def cartSummary(request):
    return render(request, 'cartSummary.html', {})

def cartAdd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(models.Product, id=product_id)
    cart.add(product=product)
    cart_quantity = cart.__len__()
    # response = JsonResponse({'Name':product.ProdName})
    # return response
    response = JsonResponse({'Quantity':cart_quantity})
    return response

def cartUpdate(request):
    pass

def cartDelete(request):
    pass