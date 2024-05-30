from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from userAuth.models import User

@csrf_exempt
@login_required
def user_id(request):
    user = request.user
    user_data = {
        'id': user.id,
        'username': user.username,
    }
    return JsonResponse(user_data)
