from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('details_games.urls')),
    path('', include('more_games.urls')),
    path('', include('login.urls')),
    path('', include('register.urls')),
    
]
