from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Product, Feedback, Brand
from .forms import FeedbackForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string



# Create your views here.
def index(request):
    # To get only 4 records or objects in order of the id in ascending order
    products = Product.objects.all().order_by('id')

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

    reviewform = FeedbackForm()
    make_review = True

    if request.user.is_authenticated:
        user_review_count = Feedback.objects.filter(user=request.user, product_id=product).count()

        if user_review_count > 0:
            make_review =False
    context = {
        'product':product,
        'reviewform': reviewform,
        'make_review': make_review
    }
    return render(request, 'products/product.html', context)

def ajax_form(request, pk):

    product = Product.objects.get(pk=pk)

    user = request.user

    review = Feedback.objects.create(
        user = user,
        name = request.POST['name'],
        rating = request.POST['rating'],
        product_id = product,
        text = request.POST['text'],
    )

    context = {
        'user': user.username,
        'name': request.POST['name'],
        'rating': request.POST['rating'],
        'text': request.POST['text']
    }

    return JsonResponse(
        {
            'bool': True,
            'context': context,
        }
    )





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


def checkbox_view(request):
#    products = request.GET.getlist('product[]')
    brands = request.GET.getlist('brand[]')
    print(brands)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    products = Product.objects.all().order_by('-id').distinct()

    if len(brands) > 0:
        products = products.filter(brand_id__id__in=brands).distinct()
        if products:
            print(products)


    context = {
        'products': products,
    }

    data = render_to_string('products/async/product.html', context)

    return JsonResponse({'data': data})