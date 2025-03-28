#!/bin/bash

# Borras todas las imagenes sin etiqueta:
docker image prune -a

# borra todos los contenedores detenidos
docker container prune

# Borra todos los volumenes no utilizados
docker volume prune

# Borra todas las imágenes, contenedores y volúmenes no utilizados
docker system prune

# Borra todo el caché de compilación:
docker builder prune
