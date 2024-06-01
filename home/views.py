from django.shortcuts import render

def home(request):
    username = request.session.get('username')
    authenticated = False
    
    if username:
        authenticated = True
    
    context = {
        'authenticated': authenticated
    }
    
    return render(request, 'home.html', context)