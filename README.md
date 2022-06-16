# Introduccion a Django

## Instrucciones:
### Iniciar entorno virtual y correr los requiremnts.txt

*  Instala entorno virtual global.
    * sudo apt-get install python3-venv
* Instala el entorno virtual en la carpeta.
    * python3 -m venv venv 
* Activa el entorno virtual.
    * source venv/bin/activate
* Instala los requerimientos de la app.
    * pip install -r requirements.txt

### Corre el framework Django:

* Inicia django framework
    * django-admin startproject django_introductionapp (django_introductionapp es el nombre del proyecto)

### Corre el servidor (software)
#### Dentro de la carpeta secundaria ingresa lo siguiente:
* ls -> Deberías poder visualizar otra carpeta llamada igual a la actual y el archivo manage.py
* Corre el servidor.
    * python3 manage.py runserver

### Crear carpeta para la aplicación
* python3 manage.py startapp polls --> crea la carpeta polls para trabajar en la app y el archivo db.sqlite3

### Notas
- manage.py --> Inicia los procesos de conexión de django con la app
- wsgi.py - asgi.py --> conjunto de archivos que son para el deploy de la app
- Los proyectos de django son un conjunto de aplicaciones.