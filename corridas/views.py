from django.http import HttpResponse
from django.shortcuts import render
from .models import Motorista
from django.contrib.gis.geos import Point

# Create your views here.
def pedir_corrida(request):
    motorista = Motorista.objects.first()
    ponto_cliente = Point(-50.494429838233788, - 26.189291919966858)
    motoristas_proximos = 
    return HttpResponse(motorista.localizacao)
