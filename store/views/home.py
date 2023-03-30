from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import category

# Create your views here.

# This function is responsible for index page


def index(request):

    products = None
    categories = category.get_all_categorys()

    categoryID = request.GET.get('category')
    if categoryID:
        # Fatch the product buy category
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        # Fatch the all products
        products = Product.objects.all()

    data = {}
    data['products'] = products
    data['categorys'] = categories

    return render(request, 'index.html', data)
