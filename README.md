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
- Se recomienda tambien tener insataladas las extenciones de python y django en VScode
    -   "emmet.includeLanguages": {
            "html": "django-html"
        } --> en el archivo settings.json de VScode para incluir html a la extención django.

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

------------------------------------
### Desarrollo
------------------------------------

#### Creación de modelos - ORM
- Una vez creados los modelos en models.py configurar settings.py en la sección de installed_apps para mandar a llamar la app polls, una vez hechos los cambios ejecutar:
    - python3 manage.py makemigrations polls --> Para crear los documentos de las conexiones.
    - python3 manage.py migrate --> Para aplicar los documentos de las configuraciones. (tiene que mandar los OK de los modelos y en este caso crea el archivo 0001_initial.py en la carpeta migrations)
    - Si deseas cambiar/editar algun modelo hay que volver a crear las migraciones y corres las migraciones

#### Consola interactiva de Django
- python3 manage.py shell --> Corre la terminal de django
- from polls.models import Choice, Question --> Para importar los modelos desde la terminal interactiva. (no debe arrojar nada)
- from django.utils import timezone --> Para crear objetos datetime y trabajar con ellos desde consola.

#### Administrador Django
- python3 manage.py createsuperuser --> Crea usuario y contraseña para el administrador.
    - Advertencia: Guardar bien los datos de administrador.

### Templates
Tendremos que crear una carpeta llamada templates dentro de polls y dentro de esa carpeta (templates) tendremos que crear otra carteta llamada polls Ejemplo:
- django-introductionapp
    - django-introductionapp
        - polls
            - templates
                - polls

### Tests
Despues de programar los test, necesitaremos correrlos.
- python3 manage.py test polls
- Pasos a seguir para los test
    - Identificar el problema
    - Crear el test
    - Correr el test
    - Arreglar el problema
    - Correr el test nuevamente para ver si se resolvió.

------------------------------------
### Fin - Desarrollo
------------------------------------
------------------------------------
### Bases de Datos
------------------------------------

INSERT de datos a través de la terminal interactiva de django:

- Question(question_text="¿Quién es el mejor profesor del IMC?", pub_date=timezone.now()).save() --> Ingresa el question_text en el objeto Question.
    - Para resolverlo con variables:
        - q = Question(question_text="¿Quíen es el mejor programador de python?", pub_date=timezone.now()) --> En la variable q dentro de consola almacenamos la respuesta de una pregunta.
        - q.save() --> Método que guarda lo que está en la variable q que en este caso se guardaría en la tabla questions de la DB
        - q --> Te dice que contiene la variable q
        - q.question_text --> Muestra el texto de la pregunta. ver más opciones en models.py

Querys de la base de datos.

- Todas las consultas se pueden almacenar en variables.
- Question.objects.all() --> Muestra todos los objetos de la clase.
- Question.objects.get(pk=1) --> Muestra la condición seleccionada, en este caso la PrimaryKey 1
- Question.objects.filter(question_text__startswith="¿Quién") --> Muestra un listado a través de la condición seleccionada, en este caso todas las question_text que inicien con "¿Quién"

Querys con variables.

- Considerando que "q" es una variable con una consulta guardada --> q = Question.objects.get(pk=3)
    - q.choice_set.create(choice_text="Guillermo Cacho", votes=0) --> Guardaría en la pregunta pk=3 la opción Guillermo Cacho como una choice_text
    - q.choice_set.all() --> Muestra el contenido de una llave foranea, para este ejemplo mostraría las respuestas de la pregunta con la primarykey=3
    - q.choice_set.count() --> Muestra el conteo en número de las respuestas existentes dentro de q
    - Choice.objects.filter(question__pub_date__year=timezone.now().year) --> Muestra el resultado de todas las respuestas que cumplan con la condición, en este caso un listado de las respuestas publicadas este año.

------------------------------------
### Fin - Bases de Datos
------------------------------------
------------------------------------
### Notas Extra
------------------------------------
- manage.py --> Inicia los procesos de conexión de django con la app
- wsgi.py - asgi.py --> conjunto de archivos que son para el deploy de la app
- Los proyectos de django son un conjunto de aplicaciones.
- ORM -> Object Relational Mapping: Sirve para replicar la estructura de una RDB a través de POO
    - RDB -> Base de datos relacional
    - POO -> Programación orientada a objetos
        - Las clases podrían traducirse a tabla, y los atributos a cada columna de la tabla en la bd. (clase usuario -> atributos id, nombre, password)
- Models.py --> Se podría decir que este archivo es nuestra base de datos en python.
- QuerySet[] --> Es un conjunto de datos de la base de datos.
- MTV --> Model Template View 
- Django Web App --> Permite trabajar el back-end y el front-end.
    - Front-End --> Templates
    - Back-End --> Views: Está conformada por funciones y clases.
        - Función --> Function Based Views
        - Clase --> Generic Views
    - Ejemplos View --> En una app como twitter cada una de las siguientes serían vistas diferentes: Home, Tweet, Setting, Messages.
- {% csrf_token %} --> Es para darle seguridad al formulario (ver detail.html)
- forloop.counter --> Es una opción de django para crear un contador que incremente con cada vuelta (ver detail.html)
- Generic View
    - List View --> Para poder traer varios elementos de la base de datos, renderizar y mostrar
    - Login View --> Para crear logins
    - Logout View --> Para hacer logouts
    - Create View --> Para crear vistas
    - Update View --> Para modificar un perfil de usuario por ejemplo
    - Form View --> Para crear por ejemplo un hilo en twitter
    - Delete View --> Para borrar un tweet por ejemplo.
    - http://ccbv.co.uk/
- tests --> Son funciones que verifican que tu código opere correctamente.
    - TDD --> Test Driven Development
    - Coverage --> Cumplir con todos los test necesarios para la app
    - Consejos extra:
        - Más tests es mejor, aunque parezca lo contrario
        - Crear una clase para cada modelo o vista testeada
        - Establece nombres de métodos de test los más descripticos posibles
------------------------------------
### Fin - Notas Extra
------------------------------------
### Retos extra
- Tests
    - Crear los tests para Results View
    - Asegurarse de que no se pueden crear Questions sin Choices
    - Crear los tests respectivos
------------------------------------
### END
------------------------------------