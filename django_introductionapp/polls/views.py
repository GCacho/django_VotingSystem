from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect #permite ejecutar respuesta HTTP
from django.urls import reverse

from .models import Question, Choice

# Create your views here.
def index(request): #Este request viene el import HttpResponse
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list # Para que hacer disponible esta variable en el template
    }) #render lleva 3 parametros 1-request, 2-template, 3-contexto


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #si existe el id continua, si no, regresa el error 404, esta funcion se importo de django
    return render(request, "polls/detail.html", {
        "question": question
    })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        "question": question
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #si encuentra la pregunta continua de lo contrario 404
    try: 
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) # choice viene de detail.html en input
    except (KeyError, Choice.DoesNotExist): # Por si el usuario envia el formulario vacio, hay que importar choice
        return render(request, "polls/detail.html", {
            "question":question,
            "error_message": "No elegiste una respuesta",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) # HttpResponseRedirect es para que el usuario no envíe su formulario 2 veces.
