# Introduccion a Django

## Instrucciones - Se recomienda ir paso a paso por commit
------------------------------------
### Instalación básica
------------------------------------
#### Iniciar entorno virtual y correr los requiremnts.txt

-  Instala entorno virtual global.
    - sudo apt-get install python3-venv
- Instala el entorno virtual en la carpeta.
    - python3 -m venv venv 
- Activa el entorno virtual.
    - source venv/bin/activate
- Instala los requerimientos de la app.
    - pip install -r requirements.txt

#### Corre el framework Django:

- Inicia django framework
    - django-admin startproject django_introductionapp (django_introductionapp es el nombre del proyecto)

#### Corre el servidor (software)
##### Dentro de la carpeta secundaria ingresa lo siguiente:
* ls -> Deberías poder visualizar otra carpeta llamada igual a la actual y el archivo manage.py
* Corre el servidor.
    * python3 manage.py runserver

#### Crear carpeta para la aplicación
* python3 manage.py startapp polls --> crea la carpeta polls para trabajar en la app y el archivo db.sqlite3
------------------------------------
### Fin de instalación básica
------------------------------------
#### Creación de modelos - ORM
- Una vez creados los modelos en models.py configurar settings.py en la sección de installed_apps para mandar a llamar la app polls, una vez hechos los cambios ejecutar:
    - python3 manage.py makemigrations polls --> Para crear los documentos de las conexiones.
    - python3 manage.py migrate --> Para aplicar los documentos de las configuraciones. (tiene que mandar los OK de los modelos y en este caso crea el archivo 0001_initial.py en la carpeta migrations)
    - Si deseas cambiar/editar algun modelo hay que volver a crear las migraciones y corres las migraciones

#### Consola interactiva de Django
- python3 manage.py shell --> Corre la terminal de django
- from polls.models import Choice, Question --> Para importar los modelos desde la terminal interactiva. (no debe arrojar nada)
- Question.objects.all() --> Muestra los objetos de la clase.
- from django.utils import timezone --> Para crear objetos datetime.
- q = Question(question_text="¿Quíen es el mejor programador de python?", pub_date=timezone.now()) --> En la variable q dentro de consola almacenamos la respuesta de una pregunta.
- q.save() --> Método que guarda lo que está en la variable q que en este caso se guardaría en la tabla questions de la DB
- q --> Te dice que contiene la variable q
- q.question_text --> Muestra el texto de la pregunta. ver más opciones en models.py


#### Notas
- manage.py --> Inicia los procesos de conexión de django con la app
- wsgi.py - asgi.py --> conjunto de archivos que son para el deploy de la app
- Los proyectos de django son un conjunto de aplicaciones.
- ORM -> Object Relational Mapping: Sirve para replicar la estructura de una RDB a través de POO
    - RDB -> Base de datos relacional
    - POO -> Programación orientada a objetos
        - Las clases podrían traducirse a tabla, y los atributos a cada columna de la tabla en la bd. (clase usuario -> atributos id, nombre, password)
- Models.py --> Se podría decir que este archivo es nuestra base de datos en python.
- QuerySet[] --> Es un conjunto de datos de la base de datos.