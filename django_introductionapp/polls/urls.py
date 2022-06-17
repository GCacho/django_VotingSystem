from django.urls import URLPattern, path
from . import views

app_name = "polls"
urlpatterns = [ # Conexión con urls de la carpeta principal del proyecto.
    #ex: /polls/ --> Ingresas al index
    path('', views.index, name="index"), #Se recibe de views.py y se "carga" a urls.py de la carpeta del proyecto.
    #ex: /polls/3/ --> permite acceder a la pregunta número 3
    path('<int:question_id>/esta/nueva/pagina/arregla/su/url/sola', views.detail, name="detail"), # '<int:question_id>/' es para pasar parametros a través de la url
    #ex: /polls/3/results/
    path('<int:question_id>/results/', views.results, name="results"),
    #ex: /polls/3/vote/
    path('<int:question_id>/vote/', views.vote, name="vote"),
]