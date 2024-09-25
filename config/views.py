from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({
            'Criação e Lista de Atores': reverse('Atores:ator_create_list', request=request),
            'Detalhes, Atualização e Exclusão de Atores': reverse('Atores:ator_detalhes', kwargs={'pk': 1}, request=request),
            'Criação e Lista de filmes': reverse('Filmes:filme_create_list', request=request),
            'Detalhes, Atualização e Exclusão de filmes': reverse('Filmes:filme_detail_list', kwargs={'pk': 1}, request=request),
            'Estatísticas de filmes': reverse('Filmes:filme_statistics', request=request),
            'Criação e Lista de gêneros': reverse('Generos:genero_create_list', request=request),
            'Detalhes, Atualização e Exclusão de gêneros': reverse('Generos:genero_detalhes', kwargs={'pk': 1}, request=request),
            'Criação e Lista de reviews': reverse('Reviews:reviews_create_list', request=request),
            'Detalhes, Atualização e Exclusão de reviews': reverse('Reviews:reviews_detalhes', kwargs={'pk': 1}, request=request),
            'Obtenção de token de validação': reverse('Authentication:token_obtain_pair', request=request),
            'Atualização de token de validação': reverse('Authentication:token_refresh', request=request),
            'Verificação de token de validação': reverse('Authentication:token_verify', request=request),
        })
