from django.shortcuts import render
from stats.models import UserStats
from django.db import models

def stats(request):
    username = request.session.get('username')
    authenticated = False
    userStats = None
    
    if username:
        authenticated = True
        userStats = UserStats.objects.get(user__username=username)
        
    worldwideStats = UserStats.objects.aggregate(
        playtime = models.Sum('playtime'),
        levelsCompleted = models.Sum('levels_completed'),
        kills = models.Sum('kills'),
        deaths = models.Sum('deaths')
    )
        
    context = {
        'authenticated': authenticated,
        'userStats': userStats,
        'worldwideStats': worldwideStats
    }

    return render(request, 'stats.html', context)
