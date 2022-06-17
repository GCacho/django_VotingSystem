from django.contrib import admin
from .models import Choice, Question

# Register your models here.

class ChoiceInline(admin.StackedInline): # Para agregar la opción de poner respuestas en las preguntas
    model = Choice
    extra = 3       # Habrá 3 espacios para llenar

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"] #D efine el orden de los campos en el admin
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently") # Añade campos en la seccion de preguntas en el admin
    list_filter = ["pub_date"] # Filtro sencillo por fecha de publicación
    search_fields = ["question_text"] # Crea un cuadro de búsqueda.

admin.site.register(Question, QuestionAdmin) #H ereda los fields de QuestionAdmin