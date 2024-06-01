from django.shortcuts import render, redirect
from stats.models import UserStats
from userAuth.forms import LoginForm, RegisterForm
from userAuth.models import User

def register(request):
    authenticated = 'username' in request.session
    message = ""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = userExists(data)
            if user:
                message = "Usuario ya existente"
            elif user is None:
                user = User(username=data['username'], email=data['email'], password=data['password'])
                user.save()
                UserStats.objects.create(user=user)
                return redirect('login')
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
        'message': message,
        'authenticated': authenticated
    }
    return render(request, 'register.html', context)

def login(request):
    authenticated = 'username' in request.session
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = userExists(data)
            if user is None:
                message = "Usuario no encontrado"
            else:
                request.session['username'] = user.username
                return redirect('home')
    else:
        form = LoginForm()
    
    context = {
        'form': form,
        'message': message,
        'authenticated': authenticated
    }
    return render(request, 'login.html', context)

def userExists(data):
    try:
        return User.objects.get(username=data['username'], password=data['password'])
    except User.DoesNotExist:
        return None

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect("home")
