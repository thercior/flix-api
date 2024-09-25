from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({
            'atores': reverse('Atores:ator_create_list', request=request),
            'atores-detalhe': reverse('Atores:ator_detalhes', kwargs={'pk': 1}, request=request),
            'filmes': reverse('Filmes:filme_create_list', request=request),
            'filmes-detalhe': reverse('Filmes:filme_detail_list', kwargs={'pk': 1}, request=request),
            'filmes-estatísticas': reverse('Filmes:filme_statistics', request=request),
            'gêneros': reverse('Generos:genero_create_list', request=request),
            'gêneros-detalhe': reverse('Generos:genero_detalhes', kwargs={'pk': 1}, request=request),
            'reviews': reverse('Reviews:reviews_create_list', request=request),
            'reviews-detalhe': reverse('Reviews:reviews_detalhes', kwargs={'pk': 1}, request=request),
            'obter_token': reverse('Authentication:token_obtain_pair', request=request),
            'refresh_token': reverse('Authentication:token_refresh', request=request),
            'verify_token': reverse('Authentication:token_verify', request=request),
        })
