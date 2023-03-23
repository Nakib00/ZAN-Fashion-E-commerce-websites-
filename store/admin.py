from django.contrib import admin
from .models.product import Product
from .models.category import category
from .models.coustomer import coustomer

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','Category']

class CategoryProduct(admin.ModelAdmin):
    list_display = ['name']
    
# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(category, CategoryProduct)
admin.site.register(coustomer)