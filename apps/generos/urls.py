from django.urls import path
from .views import *

app_name = 'Generos'

urlpatterns = [
    # Detalhes de um genero
    path('generos/', genero_create_list_view, name='genero_lista')
]
