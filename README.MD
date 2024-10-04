CRUD AllMeals para Prueba Técnica de SimpliLatam

-----------------------------------------------------------------

***Prerequisitos de ejecución***

Se debe tener instalado:

-Python 3.8 o alguna version superior (https://www.python.org/downloads/)
-Git (https://git-scm.com/downloads), para clonar el repo
-pip, para administrar los paquetes de Python
-Virtualenv, para entorno virtual (pip install virtualenv)
-Django (pip install django)

-----------------------------------------------------------------

***Pasos previos a la ejecución***

Clonar el repositorio con Git, a traves de la terminal:
https://github.com/fdezkaren/AllMealSimpliLatam.git

Crear el entorno virtual:
En la terminal, ingresar: python -m venv env

Activar el entorno virtual:
env\Scripts\activate


Nota:
Si aparece un error indicando que la ejecución de scripts estpa deshabilitada, se debe acceder a Powershell como administrador e ingresar:

Set-ExecutionPolicy RemoteSigned

Frente a la pregunta de si se está seguro responder con Y si está en inglés o S si está en español, luego intentar activar nuevamente con:

.\venv\Scripts\Activate

-----------------------------------------------------------------

***Migrar BD***

En la terminal, ejecutar:
python manage.py makemigrations

Y posteriormente:
python manage.py migrate

Para continuar, crear un superusuario para el panel de admin de Dajngo con el comando:
python manage.py createsuperuser

Y seguir las instrucciones em pantalla.

-----------------------------------------------------------------

***Ejecutar servidor***

Una vez finalizados todos los pasos previos, ejecutar en la terminal:
python manage.py runserver

Y si todo esta correctamente ejecutado, se podrá visualizar el servidor en:

http://127.0.0.1:8000/

Si por algún motivo necesita ingresar al panel de administración de Django, esto se realiza en la URL:
http://127.0.0.1:8000/admin/
