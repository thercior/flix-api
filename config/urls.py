from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import APIRootView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', APIRootView.as_view(), name='api-root'),
    path('api/v1/', include('apps.generos.urls', namespace='Generos')),
    path('api/v1/', include('apps.atores.urls', namespace='Atores')),
    path('api/v1/', include('apps.filmes.urls', namespace='Filmes')),
    path('api/v1/', include('apps.reviews.urls', namespace='Reviews')),
    path('api/v1/', include('apps.authentication.urls', namespace='Authentication')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
