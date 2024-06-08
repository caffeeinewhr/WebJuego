from django.contrib import admin
from django.urls import include, path
from home.views import home
from play.views import play
from cards.views import cards
from about.views import about
from stats.views import stats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('userAuth.urls')),
    path('home/', home, name='home'),
    path('play/', play, name='play'),
    path('cards/', cards, name='cards'),
    path('stats/', stats, name='stats'),
    path('about/', about, name='about'),
]
