from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse #permite ejecutar respuesta HTTP

# Create your views here.
def index(request): #Este request viene el import HttpResponse
    return HttpResponse("Página principal de Votaciones") #Se manda a urls.py


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")