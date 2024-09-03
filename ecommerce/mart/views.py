from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import csv

# Create your views here.
def index(request):
    if request.method == 'POST':
        id = request.POST.get('product_id')  
        product = None

        with open('mart/products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id'] == id:
                    product = row
                    break
        if product:
            request.session['cart'] += [product]
            return HttpResponseRedirect(reverse('cart:index'))

    request.session['cart'].clear()    
    with open('mart/products.csv', 'r') as file:
        reader = csv.DictReader(file)
        products = list(reader)
        
    return render(request, 'mart/index.html', {
        'products': products
    })
   