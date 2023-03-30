from django.shortcuts import render, redirect
# This madule use for making password hash
from django.contrib.auth.hashers import make_password, check_password
from store.models.coustomer import coustomer
from django.views import View

# This Class is responsible for login page


class Login(View):
    # GET Request
    def get(self, request):
        return render(request, 'login.html')

    # POST Request
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        # This function is check user email and get it from the database and store it in coustomers
        coustomers = coustomer.get_coustomer_by_email(email)
        
        error_massage = None
        # If email is exigst then check the password
        if coustomers:
            flag = check_password(password, coustomers.password)
            if flag:
                
                # Take user data using the session and cookies
                request.session['coustomer_id'] = coustomers.id
                request.session['email'] = coustomers.email
                
                return redirect('homepage')
            else:
                error_massage = 'Email and Password invalid !!'
        else:
            error_massage = 'Email and Password invalid !!'
        return render(request, 'login.html', {'error': error_massage})
