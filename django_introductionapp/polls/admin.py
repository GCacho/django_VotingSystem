from django.contrib import admin
from .models import Choice, Question

# Register your models here.

class ChoiceInline(admin.StackedInline): # Para agregar la opción de poner respuestas en las preguntas
    model = Choice
    extra = 3       # Habrá 3 espacios para llenar

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"] #Define el orden de los campos en el admin
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin) #Hereda los fields de QuestionAdmin