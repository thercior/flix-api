from django.urls import path
from filmes.views import *

app_name = 'Filmes'

urlpatterns = [
    # URLs do app Filmes
    path('filmes/', FilmeCreateListView.as_view(), name='filme_create_list'),
    path('filmes/<pk>/', FilmeDetailUpdateDeleteView.as_view(), name='filme_detail_list'),
    path('filmes/statics/', FilmeStaticsView.as_view(), name='filme_statics')
]
