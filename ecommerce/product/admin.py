from django.contrib import admin
from .models import Product, Category, SubCategory, ProductType, Usage

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductType)
admin.site.register(Usage)
