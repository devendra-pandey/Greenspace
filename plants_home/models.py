from django.db import models
from PIL import Image
import uuid 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, blank=False)


class Gallery(models.Model):
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    about = models.CharField(max_length=300, blank=False)


class Home_header_image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content= models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='gallery/')
    page_name = models.CharField(max_length=255, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Page_images(models.Model):
    title = models.CharField(max_length=50, blank=True)
    content= models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='page/')
    page_name = models.CharField(max_length=255, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=20, blank=False)
    about = models.CharField(max_length=300, blank=False)
    price= models.CharField(max_length=20, blank=False)
    quantity = models.CharField(max_length=10, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Contact_us(models.Model):
    email_id = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    contact_number = models.CharField(max_length=10, blank=True)
    description= models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='contact_us/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    image = models.ImageField(upload_to='cart/')
    name = models.CharField(max_length=20, blank=False)
    about = models.CharField(max_length=300, blank=False)
    price= models.CharField(max_length=20, blank=False)
    quantity = models.CharField(max_length=10, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

class Order(models.Model):
    product_id = models.CharField(max_length=50, blank=True)    
    image = models.ImageField(upload_to='order/')
    name = models.CharField(max_length=20, blank=False)
    about = models.CharField(max_length=300, blank=False)
    price= models.CharField(max_length=20, blank=False)
    quantity = models.CharField(max_length=10, blank=False)
    ordered_at = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    name = models.CharField(max_length=20, blank=False)
    street = models.CharField(max_length=20, blank=False)
    Area = models.CharField(max_length=20, blank=False) 
    city = models.CharField(max_length=20, blank=False)
    pincode = models.CharField(max_length=20, blank=False)
    state = models.CharField(max_length=20, blank=False)
