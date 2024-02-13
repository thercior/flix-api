from django.urls import path
from filmes.views import FilmeCreateListView, FilmeDetailUpdateDeleteView, FilmeStatisticsView

app_name = 'Filmes'

urlpatterns = [
    # URLs do app Filmes
    path('filmes/', FilmeCreateListView.as_view(), name='filme_create_list'),
    path('filmes/<int:pk>/', FilmeDetailUpdateDeleteView.as_view(), name='filme_detail_list'),
    path('filmes/statistics/', FilmeStatisticsView.as_view(), name='filme_statistics'),
]
