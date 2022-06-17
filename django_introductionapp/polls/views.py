from django.shortcuts import render
from django.http import HttpResponse #permite ejecutar respuesta HTTP

from .models import Question

# Create your views here.
def index(request): #Este request viene el import HttpResponse
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list # Para que hacer disponible esta variable en el template
    }) #render lleva 3 parametros 1-request, 2-template, 3-contexto


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")