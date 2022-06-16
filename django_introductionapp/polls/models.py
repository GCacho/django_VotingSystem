from django.db import models

# Create your models here.
class Question(models.Model): #crea el modelo con el import models
    # id - Lo crea el framework de manera automática.
    question_text = models.CharField(max_length=200) #lo convierte en varchar
    pub_date = models.DateTimeField("date published")

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Es la llave foranea de Question y eliminará toda la linea en caso de necesitarse en forma de cascada
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)