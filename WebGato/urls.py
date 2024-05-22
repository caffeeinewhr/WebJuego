from django.contrib import admin
from django.urls import path
from home.views import home
from play.views import play
from cards.views import cards
from about.views import about
from stats.views import stats
from userAuth.views import register, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('play/', play, name='play'),
    path('cards/', cards, name='cards'),
    path('stats/', stats, name='stats'),
    path('about/', about, name='about'),
]
