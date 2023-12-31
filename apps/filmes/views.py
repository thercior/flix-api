from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from config.permissions import GlobalPermissions
from filmes.serializers import FilmeSerializer
from filmes.models import Filme

# Create your views here.
class FilmeCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    
class FilmeDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
