from .models import Product, Brand
from django.db.models import Min, Max


def default(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    min_max_price = products.aggregate(Min('price'), Max('price'))


    return {
        'products': products,
        'brands': brands,
        'min_max_price': min_max_price,
    }