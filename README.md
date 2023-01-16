# API Rest Dajngo - Store

> URL Api producción = https://apiomni-production.up.railway.app/


- URL Document Api = https://app.swaggerhub.com/apis-docs/JEFERSONRR_1/Api_Store_omni.pro/1.0.0#/


El proyecto esta desplegado en un servidor web de Raiwail, desarrollada con tecnologia Python (Django).

## Tecnologias
- [Django] - es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como modelo–vista–controlador.

## Requerimientos

- Django==3.2.4
- psycopg2
- gunicorn==20.1.0
- pytz==2021.1
- sqlparse==0.4.1
- whitenoise==5.2.0
- django-environ==0.7

## Instalación

El proyecto requiere de  Python v3.10.0 (La version 3.9 tambien es compatible) para su funcionamiento correcto.

> Nota: Se requiere crear un entorno virtual por lo cual se debe instalar la libreria virtualenv

Instalando liberia para la creación de entornos virtuales.
```sh
pip install virtualenv
```

> Nota: Realizamos  la clonación del proyecto y  Situados en la carpeta raiz del proyecto

Creando el entorno virtual
```sh
python -m venv virtualenvs
```

Esto nos generará una carpeta con el  nombre virtulenvns, nos dirigimos a la ruta virtualenvs/Scrips/

Activando el entorno virtual.
```sh
activate
```
> Nota: Una vez activado el entorno virtual por la misma consola nos situados en la carpeta raiz del proyecto

Instalando librerias de Django y python necesarias para el funcionamiento de la api-rest.
```sh
pip install -r requirements.txt
```

> Nota: Una vez instaladas las librerias y situados en la carpeta raiz del proyecto 

Corriendo el proyecto de forma local
```sh
python manage.py runserver 
```
>Nos situamos en el navegados y buscamos localhost:8000

> **Autor :**
> - jeferson Rodriguez Ramirez, jefersonrr04@gmail.com

   [NodeJs]: <https://nodejs.org/es/docs/>
   [Django]: <https://docs.djangoproject.com/en/3.2/>
   [ReactJs]: <https://es.reactjs.org/docs/getting-started.html>


