from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.generos.urls', namespace='Generos')),
    path('', include('apps.atores.urls', namespace='Atores')),
    path('', include('apps.filmes.urls', namespace='Filmes')),
]
