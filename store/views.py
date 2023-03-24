from django.shortcuts import render, redirect
from django.http import HttpResponse
# This madule use for making password hash
from django.contrib.auth.hashers import make_password,check_password
from .models.product import Product
from .models.category import category
from .models.coustomer import coustomer


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


# Validation caking functions for singup page caoustomer registration
def validateCoustomer(coustomer_object):
    
    # Validations
        error_message = None

        if (not coustomer_object.first_name):
            error_message = "First name Required !!"
        elif (len(coustomer_object.first_name) < 4):
            error_message = "First name must be 4 char long"
        elif (not coustomer_object.last_name):
            error_message = "Last name Required !!"
        elif (len(coustomer_object.last_name) < 3):
            error_message = "Last name must be 3 char long"
        elif (not coustomer_object.phone_number):
            error_message = "Phone Required !!"
        elif (not coustomer_object.email):
            error_message = "Email Required !!"
        # Check same email address is already exists or not
        elif coustomer_object.isexist():
            error_message = "Email address already registered.."
        elif (not coustomer_object.password):
            error_message = "Password Required !!"
        elif (len(coustomer_object.password) <= 6):
            error_message = "Password Required 6 Uper len password !!"
        
        return error_message
    
# when post mathod is available then this function is called and registers the new coustomer object
def register_user(request):
    
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phonenumber')
    email = postData.get('email')
    password = postData.get('password')

    # store the data from user in ta value dictionary
    value = {
        'firstname': first_name,
        'lastname': last_name,
        'phone': phone,
        'email': email
    }

    # Create a coustomer object
    coustomer_object = coustomer(
        first_name=first_name, last_name=last_name, phone_number=phone, email=email, password=password)

    # call validation function for checking the coustomer data
    error_message = validateCoustomer(coustomer_object)

    # Saving
    if not error_message:
            
        # Make the user password hash using make password function
        coustomer_object.password = make_password(coustomer_object.password)
            
        # call the coustomer object and save the data in database
        coustomer_object.register_user()

        # When the user singup then Home page will be loaded and shown by using this return 'homepage' is the mane of the index page
        return redirect('homepage')

    else:
        # Data dictionary send the singup page
        data = {
            'error': error_message,
            'values': value
        }
        return render(request, 'singup.html', data)


# This function is responsible for singup page
def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html')
    else:
        # Call the register_user function for registration new user when Mathod id post
        return register_user(request)
