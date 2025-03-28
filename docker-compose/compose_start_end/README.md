# Orden de encidio y apagado  

El .yml establece un orden de encendido y apagado:  

1. El backend inicia primero, cuando ya esté iniciado:

2. eL frontend se inicia.

## funciones de docker  

- backend: envía un json, es como una api: donde el js del front-end lo recibe.  

- frontend: Imprime el json que lo imprime en formato de API  

Es por eso que, el backend debe ejecutarse primero, y el front al final  


## Para construir la imágen:  

para levantar la imágen: `docker compose up --build`.  

## diferencia entre ctrl+c y docker compose down  

- Si usas el comando `docker compose down`borras los volumenes, redes, y demás que puede ocupar espacio.

- Si usas ctrl+c, solo lo detienes