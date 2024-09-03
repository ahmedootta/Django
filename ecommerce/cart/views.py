from django.shortcuts import render

# Create your views here.
def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = []

    return render(request, 'cart/index.html',{
        'cart': request.session['cart']
    })
   