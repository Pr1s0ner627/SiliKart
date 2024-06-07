from django.shortcuts import render

# Create your views here.
def cartSummary(request):
    return render(request, 'cartSummary.html', {})
def cartAdd(request):
    pass
def cartUpdate(request):
    pass

def cartDelete(request):
    pass