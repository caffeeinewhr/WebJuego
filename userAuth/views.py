from django.shortcuts import render, redirect

from stats.models import UserStats
from userAuth.forms import LoginForm, RegisterForm
from userAuth.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            user = userExists(data)
            
            if user:
                message = "Usuario ya existente"  
            elif user == None:
                user = User(username=data['username'], email=data['email'], password=data['password'])
                user.save()
                UserStats.objects.create(user=user)
                return redirect('login')
    else:
        form = RegisterForm()
        message = ""
    return render(request, 'register.html', {'form':form, 'message':message})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            user = userExists(data)
            
            if user == None:
                message = "Usuario no encontrado"  
            else:
                request.session['username'] = user.username
                return redirect('home')
    else:
        form = LoginForm()
        message = ""
    return render(request, 'login.html', {'form':form, 'message':message})


def userExists(data):
    try:
        return User.objects.get(username=data['username'], password=data['password'])
    except User.DoesNotExist:
        return None
    
    
def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect("home")
