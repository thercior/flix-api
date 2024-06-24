from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from config.permissions import GlobalPermissions
from atores.models import Ator
from atores.serializers import AtorSerializer


class AtorCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer

    # Aplicação campos de filtragem
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nome', 'nacionalidade']
    search_fields = ['nome', 'nacionalidade']
    ordering = ['id']
    ordering_fields = [
        'id',
        'nome',
        'nascimento',
        'nacionalidade',
    ]


class AtorDetailsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer
