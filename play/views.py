from django.shortcuts import render

def play(request):
    username = request.session.get('username')
    
    if username:
        return render(request, 'game.html', {'username': username})
        
    return render(request, 'beforeLog.html')