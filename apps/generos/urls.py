from django.urls import path
from .views import *

app_name = 'Generos'

urlpatterns = [
    # Detalhes de um genero
    path('generos/', GeneroCreateListView.as_view(), name='genero_create_list'),
    path('generos/<pk>/', GeneroDetailsUpdateDeleteView.as_view(), name='genero_detalhes'),
]
