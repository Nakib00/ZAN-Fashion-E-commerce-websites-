from .views import index,singup,login
from django.urls import path

urlpatterns = [
    path('', index, name='homepage'),
    path('singup', singup, name='singup'),
    path('login', login, name='login')
]
