import json
from django.http import JsonResponse
from stats.models import UserStats
from userAuth.models import User
from django.views.decorators.csrf import csrf_exempt

def user_exists(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'exists': True})
        except User.DoesNotExist:
            return JsonResponse({'exists': False, 'error': 'User does not exist'})

@csrf_exempt
def update_user_stats(request):
    if request.method == 'POST':
        print("Update user stats POST request received")
        data = json.loads(request.body)
        print(f"Received data: {data}")  # Debug print
        username = data.get('username')
        stats = data.get('stats', {})

        try:
            user = User.objects.get(username=username)
            print(f"User found: {user.username}")  # Debug print
            user_stats, created = UserStats.objects.get_or_create(user=user)

            if 'playtime' in stats:
                print(f"Old playtime: {user_stats.playtime}")
                user_stats.playtime = stats.get('playtime', user_stats.playtime)
                print(f"New playtime: {user_stats.playtime}")
            if 'levels_completed' in stats:
                print(f"Old levels_completed: {user_stats.levels_completed}")
                user_stats.levels_completed = stats.get('levels_completed', user_stats.levels_completed)
                print(f"New levels_completed: {user_stats.levels_completed}")
            if 'kills' in stats:
                print(f"Old kills: {user_stats.kills}")
                user_stats.kills = stats.get('kills', user_stats.kills)
                print(f"New kills: {user_stats.kills}")
            if 'deaths' in stats:
                print(f"Old deaths: {user_stats.deaths}")
                user_stats.deaths = stats.get('deaths', user_stats.deaths)
                print(f"New deaths: {user_stats.deaths}")

            user_stats.save()
            return JsonResponse({'success': True, 'message': 'User stats updated successfully'})  # Ensure success response

        except User.DoesNotExist:
            print("User does not exist.")  # Debug print
            return JsonResponse({'success': False, 'error': 'User not found'}, status=404)
        except Exception as e:
            print(f"Error: {str(e)}")  # Debug print
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

def get_user_stats(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        username = data.get('username')

        try:
            user = User.objects.get(username=username)
            user_stats = UserStats.objects.get(user=user)

            stats = {
                'playtime': user_stats.playtime,
                'levels_completed': user_stats.levels_completed,
                'kills': user_stats.kills,
                'deaths': user_stats.deaths,
            }

            return JsonResponse({'success': True, 'stats': stats})

        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User not found'}, status=404)
        except UserStats.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User stats not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)