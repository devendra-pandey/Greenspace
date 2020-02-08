from django.contrib import admin
from .models import Gallery, Home_header_image, Page_images, Product,Category, Contact_us
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



admin.site.register(Home_header_image)
admin.site.register(Gallery)
admin.site.register(Page_images)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact_us)