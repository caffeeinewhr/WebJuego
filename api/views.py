from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from userAuth.models import User

def user_id(request):
    username = request.session.get('username')
    return JsonResponse({'username': username})
