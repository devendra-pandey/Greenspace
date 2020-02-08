from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    
    path('accounts/', include('allauth.urls')), # new
]
