from django.contrib import admin
from django.urls import path
from home.views import home
from play.views import play
from cards.views import cards
from about.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('play/', play, name='play'),
    path('cards/', cards, name='cards'),
    path('about/', about, name='about'),
]
