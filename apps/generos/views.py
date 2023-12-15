import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from generos.models import Genero

# Create your views here.
@csrf_exempt
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