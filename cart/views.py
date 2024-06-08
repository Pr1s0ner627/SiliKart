from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.contrib import messages
from store import models
from django.http import JsonResponse
# Create your views here.
def cartSummary(request):
    cart = Cart(request)
    cart_prods = cart.getProd
    quantities = cart.getQuants
    totals = cart.cartTotal()
    return render(request, 'cartSummary.html', {'cart_products':cart_prods, 'quantities':quantities, 'total':totals})

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
    messages.success(request, ("Product added to cart..."))
    return response

def cartUpdate(request):
    response = JsonResponse({'error': 'Invalid request'})  # Default response for invalid requests
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        # Check if product_id and product_qty are provided and are valid integers
        if product_id and product_qty and product_id.isdigit() and product_qty.isdigit():
            product_id = int(product_id)
            product_qty = int(product_qty)

            cart = Cart(request)
            cart.update(product=product_id, quantity=product_qty)
            
            response = JsonResponse({'Quantity': product_qty})
            messages.success(request, "Cart has been updated...")
        else:
            response = JsonResponse({'error': 'Invalid product ID or quantity'})
    return response

def cartDelete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        
        response = JsonResponse({'Product':product_id})
        messages.success(request, ("Item has been deleted successfully..."))
    return response

 