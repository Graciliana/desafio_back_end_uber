from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Motorista
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

# Create your views here.
def pedir_corrida(request):
    lgn = float(request.GET.get('longitude'))
    lat = float(request.GET.get('latitude'))
    
    ponto_cliente = Point(lgn, lat, srid=4326)
    motoristas_proximos = Motorista.objects.annotate(distancia=Distance('localizacao', ponto_cliente)).filter(distancia__lte=D(km=10))
    
    if not motoristas_proximos.exists():
        return JsonResponse({'erro': 'Nenhum motorista em até 10 km'})
    
    mais_proximo = motoristas_proximos.order_by("distancia").first()
    distancia_referencia = mais_proximo.distancia
    grupo = motoristas_proximos.filter(distancia__lte=distancia_referencia + D(m=200))
    
    melhor = grupo.order_by('-avaliacao').first()
    
    return HttpResponse(melhor)
