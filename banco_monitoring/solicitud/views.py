from .logic import solicitudes_logic as slt
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.          
@csrf_exempt
def solicitudes_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            solicitud_dto = slt.get_solicitud(id)
            solicitud = serializers.serialize('json', [solicitud_dto,])
            return HttpResponse(solicitud, 'application/json')
        else:
            solicitud_dto = slt.get_solicitudes()
            solicitud = serializers.serialize('json', solicitud_dto)
            return HttpResponse(solicitud, 'application/json')

    if request.method == 'POST':
        solicitud_dto = slt.create_solicitud(json.loads(request.body))
        solicitud = serializers.serialize('json', [solicitud_dto,])
        return HttpResponse(solicitud, 'application/json')

@csrf_exempt
def solicitud_view(request, pk):
    if request.method == 'GET':
        solicitud = slt.get_solicitud(pk)
        solicitud_dto = serializers.serialize('json', solicitud)
        return HttpResponse(solicitud_dto, 'application/json') 

    if request.method == 'PUT':
        solicitud_dto = slt.update_solicitud(pk, json.loads(request.body))
        solicitud = serializers.serialize('json', [solicitud_dto,])
        return HttpResponse(solicitud, 'application/json')