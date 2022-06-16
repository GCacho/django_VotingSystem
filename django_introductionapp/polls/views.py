from django.shortcuts import render
from django.http import HttpResponse #permite ejecutar respuesta HTTP

# Create your views here.
def index(request): #Este request viene el import HttpResponse
    return HttpResponse("Hello World!") #Se manda a urls.py