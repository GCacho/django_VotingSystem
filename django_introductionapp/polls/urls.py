from django.urls import URLPattern, path
from . import views

urlpatterns = [ # Conexión con urls de la carpeta principal del proyecto.
    #ex: /polls/ --> Ingresas al index
    path('', views.index, name="index"), #Se recibe de views.py y se "carga" a urls.py de la carpeta del proyecto.
    #ex: /polls/3/ --> permite acceder a la pregunta número 3
    path('<int:question_id>/', views.detail, name="index"), # '<int:question_id>/' es para pasar parametros a través de la url
    #ex: /polls/3/results/
    path('<int:question_id>/results/', views.results, name="index"),
    #ex: /polls/3/vote/
    path('<int:question_id>/vote/', views.vote, name="index"),
]