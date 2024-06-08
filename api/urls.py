from django.urls import path
from api.views import get_user_stats, user_exists, update_user_stats

urlpatterns = [
    path('user_exists/', user_exists, name='user_exists'),
    path('update_user_stats/', update_user_stats, name='update_user_stats'),
    path('get_user_stats/', get_user_stats, name='get_user_stats'),
]