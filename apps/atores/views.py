from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from atores.models import Ator
from atores.serializers import AtorSerializer
# Create your views here.
class AtorCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer
    
class AtorDetailsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer