import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): #crea el modelo con el import models
    # id - Lo crea el framework de manera automática.
    question_text = models.CharField(max_length=200) #lo convierte en varchar
    pub_date = models.DateTimeField("date published")


    def __str__(self): #Método dunder string
        return self.question_text #Que muestre el valor del texto


    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1) #Le resta al tiempo actual un día. necesita imports de date y datetime / Si la pregunta es más reciente a 1 día entonces True


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Es la llave foranea de Question y eliminará toda la linea en caso de necesitarse en forma de cascada
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): #Método dunder string
        return self.choice_text #Que muestre el valor del texto
