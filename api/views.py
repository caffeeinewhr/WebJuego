from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from userAuth.models import User

@csrf_exempt
def user_id(request):
    username = request.session.get('username')
    if username:
        print(username)
        try:
            user = User.objects.get(username=username)
            user_data = {
                'id': user.id,
                'username': user.username,
            }
            return JsonResponse(user_data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else: 
        return JsonResponse({'error': 'User not logged in'}, status=401)
