from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.generos.urls', namespace='Generos')),
    path('api/v1/', include('apps.atores.urls', namespace='Atores')),
    path('api/v1/', include('apps.filmes.urls', namespace='Filmes')),
    path('api/v1/', include('apps.reviews.urls', namespace='Reviews')),
]
