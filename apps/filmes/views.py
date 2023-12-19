from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from filmes.serializers import FilmeSerializer
from filmes.models import Filme

# Create your views here.
class FilmeCreateListView(ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    
class FilmeDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
