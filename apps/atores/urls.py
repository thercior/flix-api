from django.urls import path
from atores.views import *

app_name = 'Atores'

urlpatterns = [
    # URLs de um ator
    path('atores/', AtorCreateListView.as_view(), name='ator_create_list'),
    path('atores/<pk>/', AtorDetailsUpdateDeleteView.as_view(), name='ator_detalhes'),
]
