from django.db import models

#if you want a relationship between moodels in differnt apps either onetoone, onetomany or manytomany relationships
#from products.models import Product

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    #if you want a relationship between moodels in differnt apps either onetoone, onetomany or manytomany relationships
    #orders = models.ManyToManyField(Product)
