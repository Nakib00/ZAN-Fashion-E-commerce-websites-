from .views import index,singup
from django.urls import path

urlpatterns = [
    path('', index, name='homepage'),
     path('singup', singup )
]
