from django.urls import URLPattern, path
from . import views

urlpatterns = [ # Conexión con urls de la carpeta principal del proyecto.
    path('', views.index, name="index") #Se recibe de views.py y se "carga" a urls.py de la carpeta del proyecto.
]