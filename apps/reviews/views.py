from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from config.permissions import GlobalPermissions
from reviews.models import Review
from reviews.serializers import ReviewListDetailSerializer, ReviewSerializer


class ReviewCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Review.objects.all()

    # Aplicação campos de filtragem
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['filme', 'stars']
    search_fields = ['filme', 'stars']
    ordering = ['id', 'filme']
    ordering_fields = [
        'id',
        'filme',
        'stars',
        'nacionalidade',
    ]

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return ReviewListDetailSerializer

        return ReviewSerializer


class ReviewDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Review.objects.all()

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return ReviewListDetailSerializer

        return ReviewSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        success_message = "Este Review foi excluído com sucesso!"
        return response.Response({"message": success_message})
