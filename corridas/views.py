from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def pedir_corrida(request):
    return HttpResponse('teste')
