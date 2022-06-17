from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect #permite ejecutar respuesta HTTP
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
# def index(request): #Este request viene el import HttpResponse
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list # Para que hacer disponible esta variable en el template
#     }) #render lleva 3 parametros 1-request, 2-template, 3-contexto


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id) #si existe el id continua, si no, regresa el error 404, esta funcion se importo de django
#     return render(request, "polls/detail.html", {
#         "question": question
#     })

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#     })

# Based Class Views o Generic Views / from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self): # es para obtener las preguntas
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by("-pub_date")[:5] #order_by es igual a filter pero ordenado / El "-" antes de pub es para ordenar de la más reciente a la más vieja / [:5] es para mostrar solo 5
    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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
