# Las capas reducen muchisimo el tamaño de las imágenes.
En lugar de tener 3 capas que actualicen el s.o y descarguen curl, al hacerlo en una capa, reduces mucho el tamaño
```
// capa 1
RUN apt update
// capa 2
RUN apt upgrade
// capa 3
RUN apt install curl
```
Al hacerlo en una sola capa, reduces el tamaño:
# Capa 2: Ejecuta el update
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* 
