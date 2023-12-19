from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from atores.models import Ator
from atores.serializers import AtorSerializer
# Create your views here.
class AtorCreateListView(ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer
    
class AtorDetailsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer