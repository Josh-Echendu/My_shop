from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.

User = get_user_model()


class Orders(models.Model):
    ORDER_CHOICES = (
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('delivered', 'Delivered')
    )
    total_amount = models.IntegerField()
    order_date = models.DateField()
    order_status = models.CharField(max_length=150, choices=ORDER_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ords')    

class Address(models.Model):
    street = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city} - {self.country}"

class Brand(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField()
    address_id = models.OneToOneField(Address, on_delete=models.Case, null=True)

    def __str__(self):
        return f"{self.title}"
    
class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    category_id = models.ManyToManyField(Category)
    # the upload_to creates a folder called 'product-img' in the 'uploads' folder created in settings.py for the images to be stored 
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name='products')
    image = models.ImageField(blank=True, upload_to='product-img')
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default=False)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_prod', null=True)

    # A field for similar product: for example if you have a product and you also want to show other related or similar products together and suggest it to our users
    suggestions = models.ManyToManyField('self') #for same model relationships we use same model relationships

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_user')
    name = models.CharField(max_length=40)
    rating = models.PositiveSmallIntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.product_id} -- Rating {self.rating}"





# To get some certain amount of records i.e to get 4 out of 5 records i.e list slicing
# Shirt.objects.all()[:4] 

# To check wether an object or a record exist or not
#Shirt.objects.filter(price=15).exists() 
# this returns a boolean

# difference between get and filter using field lookups
#get() returns only 1 object or record
#filter() returns more then one objects or record

#To filter the fields lessthan than 25 using field lookupsd
#jo = Shirt.objects.filter(price__lt=25)

#To filter the fields greater than 25
#jo = Shirt.objects.filter(price__gt=25)

#To filter the fields with an 'and' operator
#jo = Shirt.objects.filter(title='Tom Brand', is_bestseller=True) 

#To filter the fields with an 'or' operator
# from django.db.models import Q
# list = Shirt.objects.filter(Q(is_bestseller=False) | Q(name__contains = 'polo')) 

# To add records in many to many relationships
#from product.models import Category, Product 
#In [9]: classic = Category.objects.create(title='Classic', d 
#   ...: escription='this is a test description')

#In [10]: wedding = Category.objects.create(title='wedding',  
#    ...: description='this is a test description')

#In [11]: first_suit = Product.objects.get(id=1)

#In [14]: first_suit.category_id.add(classic, wedding)

#In [15]: first_suit.save()