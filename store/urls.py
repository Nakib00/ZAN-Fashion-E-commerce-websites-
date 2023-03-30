from .views import home,login,singup
from django.urls import path

urlpatterns = [
    path('', home.index, name='homepage'),
    path('singup', singup.Singup.as_view(), name='singup'),
    path('login', login.Login.as_view(), name='login')
]
