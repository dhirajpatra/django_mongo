from django.contrib import admin
from .models import Product, Producttype

# Register your models here.
admin.site.register(Producttype)
admin.site.register(Product)
