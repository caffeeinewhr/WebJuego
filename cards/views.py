from django.shortcuts import render

def cards(request):
    username = request.session.get('username')
    authenticated = False
    
    if username:
        authenticated = True
    
    context = {
        'authenticated': authenticated
    }
    
    return render(request, 'cards.html', context)