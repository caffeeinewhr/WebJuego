from django.shortcuts import render

def play(request):
    username = request.session.get('username')
    authenticated = False
    
    if username:
        authenticated = True
        
        context = {
            'username': username,
            'authenticated': authenticated
        }
        
        return render(request, 'game.html', context)
    
    context = {
        'username': '',
        'authenticated': authenticated
    }
    
    return render(request, 'beforeLog.html', context)