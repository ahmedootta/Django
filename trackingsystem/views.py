from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
import csv

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('canceled', 'Canceled'),
]

class NewOrder(forms.Form):
    id = forms.IntegerField(label='Order Id', min_value=1, max_value=15)
    name = forms.CharField(label='Order Name', min_length=2, max_length=15)
    username = forms.CharField(label='Username', min_length=2, max_length=15)
    status = forms.ChoiceField(label='Order Status', choices=STATUS_CHOICES)

# Create your views here.
def index(request):
    with open('trackingsystem/orders.csv', 'r') as file:
        reader = csv.DictReader(file)
        orders = list(reader)
        
    return render(request, 'trackingsystem/index.html', {
        'orders': orders
    })


def order(request, id):
    return render (request, 'trackingsystem/orderId.html',{
        "id": id
    })    

def add(request):
    if request.method == 'POST':
        form = NewOrder(request.POST)
        if form.is_valid():
            with open('trackingsystem/orders.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([
                    form.cleaned_data['id'],
                    form.cleaned_data['name'],
                    form.cleaned_data['username'],
                    form.cleaned_data['status']
                ])
            return HttpResponseRedirect(reverse('trackingsystem:index'))   
        else:
            return render (request, 'trackingsystem/form.html', {
                'form': form
            })      
    return render (request, 'trackingsystem/form.html', {
        'form': NewOrder()
    })    
    