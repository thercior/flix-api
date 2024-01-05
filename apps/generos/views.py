import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from generos.models import Genero
from generos.serializers import GeneroSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import response, status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class GeneroCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class GeneroDetailsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        success_message = "Gênero excluído com sucesso!"
        return response.Response({"message": success_message})

"""@csrf_exempt
def genero_create_list_view(request):
    if request.method == 'GET':
        generos = Genero.objects.all()
        data = [{'id': genero.id, 'nome': genero.nome} for genero in generos]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        novo_genero = Genero(nome=data['nome'])
        novo_genero.save()
        return JsonResponse(
            {'id': novo_genero.id, 'nome': novo_genero.nome}, 
            status=201
        )

@csrf_exempt
def genero_detalhes_view(request, pk):
    
    genero = get_object_or_404(Genero, pk=pk)
    
    if request.method == 'GET':
        data = {'id': genero.id, 'nome': genero.nome}
        return JsonResponse(data)
    
    elif request.method == 'PUT':        
        data = json.loads(request.body.decode('utf-8'))
        genero.nome = data['nome']
        genero.save()
        
        return JsonResponse(
            {'id': genero.id, 'nome': genero.nome},
            status=200
        )
        
    elif request.method == 'DELETE':
        genero.delete()
        return JsonResponse(
            {'message': 'Gênero excluído com sucesso'},
            # status=204
        )
"""