from django.urls import path
from api.views import user_id

urlpatterns = [
    path('user/', user_id, name='user-id'),
]