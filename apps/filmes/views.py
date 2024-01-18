from django.db.models import Avg, Count
from rest_framework import status, response, views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
from config.permissions import GlobalPermissions
from filmes.serializers import FilmeSerializer, FilmeStatisticsSerializer
from filmes.models import Filme
from reviews.models import Review

# Create your views here.
class FilmeCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    
class FilmeDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

# View para retorno de dados estatĩsticos do meu endpoint
class FilmeStatisticsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Filme.objects.all()
    
    def get(self, request):
        # Busca dos dados
        total_filmes = self.queryset.count()
        filmes_por_genero = self.queryset.values('genero__nome').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        media_avaliacoes = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        
        # Monta o conjunto de dados
        data = {
            'total_filmes': total_filmes,
            'filmes_por_genero': filmes_por_genero,
            'total_reviews': total_reviews,
            'media_avaliacoes': round(media_avaliacoes, 1) if media_avaliacoes else 0,
        }
        
        # Envia para o serializer para serializar o conjunto de dados
        serializer = FilmeStatisticsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        return response.Response(
            # data=data, # já vem em formato dicionário (json, serializado)
            data=serializer.validated_data, # retorna os dados que foram serializados
            status=status.HTTP_200_OK,
        )

