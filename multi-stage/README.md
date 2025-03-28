Encontraste un **dockerfile que usa multi-stage** con python 🐍:  

```
# Primera imagen para compilar 
FROM python:3.8.4-slim-buster as compile-image
# Se define una variable opcional
RUN python3 -m venv /opt/venv
# Se sobreescribe la variable path para que tenga prioridad los comandos del ambiente
ENV PATH="/opt/venv/bin:$PATH"
# Se copia unicamente el archivo de dependencias 
COPY requirements.txt /requirements.txt
# Se instalan las dependencias.
RUN pip install -r requirements.txt
# Listo, inicia el segundo contenedor 
FROM python:3.8.4-alpine3.12 AS build-image
# Se copia la carpeta venv que contiene todas las dependencias en el segundo contenedor
COPY --from=compile-image /opt/venv /opt/venv
# Se copia la aplicación
COPY . usr/src/app
# Se establece por defecto el directorio 
WORKDIR /usr/src/app
# Se agrega el directorio a las variables de ambiente.
ENV PATH="/opt/venv/bin:$PATH"
# Arranca la aplicación
ENTRYPOINT python3 main.py
```  
**aquí te cuento algunas cosas que me sorprendieron:**  
1 etapa o primer contendor  
- En esta etapa solo compila la imágen de python: instala dependencias y demás.  
- `FROM python:3.8.4-slim-buster as compile-image` la versión slim-buster te da la imagen que compila con C. Por lo que es adecuada para correr numpy, keras y todo lo relacionado con machine learning.  
- la línea `RUN python3 -m venv /opt/venv` asigna una carpeta para el entorno virtual.  
- la línea `ENV PATH="/opt/venv/bin:$PATH"` asigna el entorno virtual al path o variables de entorno de linux 🤯  (así todo corre en el entorno virtual y no en el sistema operativo del docker)  
- las dependencias se instalarán en el entorno virtual: `RUN pip install -r requirements.txt`

**2 etapa o segundo contendor**  
- La primera etapa deja el docker lleno de caché y basura que solo hace el docker más pesado. Por lo que en esta segunda etapa, se crea un nuevo docker que sí va a ser usado.  
- `FROM python:3.8.4-alpine3.12 AS build-image` descarga la imágen de python que funciona con alpine. *¡Alpine es la distro de linux más liviana que existe! 🪶* 
- la línea `COPY --from=compile-image /opt/venv /opt/venv` copia las dependencias del contenedor sucio y las pega en el directorio opt/venv (ya sabes el entorno virtual)
- aquí **SÍ** copias el proyecto `COPY . usr/src/app`, en un contenedor limpio 
- Creas el Workdir, nuevamente asignas el path para que todas las dependencias se instalen allí y `ENTRYPOINT` arranca el archivo que necesites.

