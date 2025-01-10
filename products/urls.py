from django.urls import path
from .views import index, sign_up, product_detail, search, ajax_form, checkbox_view

urlpatterns = [
    path('', index, name='home'),
    path('products/<str:brand>/<slug:product_slug>/', product_detail, name='product-detail'), 
    path('search/', search, name='search'),
    path('ajax_comment/<pk>', ajax_form, name='ajax_form'),
    # Filter product
    path('filter-products/', checkbox_view , name='filter-products'),
]
