from django.contrib import admin
from .models import Category, Product, Details


admin.site.register(Category)
admin.site.register(Details)
admin.site.register(Product)
# Register your models here.
