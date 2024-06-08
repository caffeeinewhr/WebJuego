from django.urls import path
from userAuth.views import login, logout, register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'), 
]