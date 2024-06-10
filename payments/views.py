from django.shortcuts import render

# Create your views here.
def paymentSuccess(request):
    return render(request, 'paymentSuccess.html', {})