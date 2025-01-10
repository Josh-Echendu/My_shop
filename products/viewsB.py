from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Product, Feedback, Brand
from .forms import FeedbackForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django.views import View
from django.db.models import Q



# Create your views here.
def index(request):
    # To get only 4 records or objects in order of the id in ascending order
    products = Product.objects.all().order_by('id')[:4]

    # we want to return the product in which the brand title is equal to pouya
    # suit = Product.objects.filter(brand_id__title = 'pouya')
    pouya = get_object_or_404(Brand, title='pouya')
    print(pouya)
    suits = pouya.products.all()
    print(suits)
    context = {
        'products': products,
    }

    return render(request, 'products/home2.html', context)

def sign_up(request):
    return render(request, 'products/signup2.html')

# views.py
def product_detail(request, brand, product_slug):
    product = Product.objects.get(slug=product_slug)
    print(product)
    reviews = Feedback.objects.filter(product_id=product)
    if request.method == 'GET':
        form = FeedbackForm()
        context = {
            'product': product,
            'form': form,
            'reviews': reviews
        }
        return render(request, 'products/product.html', context)
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rating = form.cleaned_data['rating']
            product = product
            text = form.cleaned_data['text']
            Feedback.objects.create(name=name, rating=rating, product_id=product, text=text)
            
            messages.success(request, 'Your feedback was submitted successfully')


            
            # This is used to clear the form after submitting the form
            #form = FeedbackForm()
        context = {
            'form':form,
            'product': product,
            'reviews': reviews
            }
        return render(request, 'products/product.html', context)
    


    # To get only 4 records or objects in order of the id in descending order
    # products = Product.objects.all().order_by(-id)[:4]

def search(request):

    # Extract q from template
    query = request.GET.get('q')

    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'products/search.html', context)


