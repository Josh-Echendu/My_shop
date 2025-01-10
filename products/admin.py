from django.contrib import admin
from .models import Brand, Product, Feedback, Address, Category, Orders

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    #To make a field read only
    #readonly_fields = ('slug', )
    list_display = ('title', 'id', 'is_bestseller')
    list_filter = ('is_bestseller',)
    search_fields = ('title', 'category', 'brand_id')

admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Address)
admin.site.register(Brand)
admin.site.register(Feedback)
admin.site.register(Product, ProductAdmin)

