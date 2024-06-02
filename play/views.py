from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def play(request):
    username = request.session.get('username')
    authenticated = False
    
    if username:
        authenticated = True
        context = {
            'username': username,
            'authenticated': authenticated
        }
        
        # Use the render function to generate the response
        response = render(request, 'index.html', context)
    else:
        context = {
            'username': '',
            'authenticated': authenticated
        }
        
        # Use the render function to generate the response
        response = render(request, 'beforeLog.html', context)
    
    # Set the necessary headers for cross-origin isolation
    response['Cross-Origin-Opener-Policy'] = 'same-origin'
    response['Cross-Origin-Embedder-Policy'] = 'require-corp'
    
    return response
