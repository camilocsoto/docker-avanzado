esta es una versión mejorada con `docker-compose.yml` de `balancear_cargas` de la carpeta raíz `./`.  

Cambios:
1. En `nginx.conf`agrega el puerto a la sección `upstream backend_servers`.  

2. Construye el docker-compose.yml para balancear las cargas en un red local de tipo bridge.  

3. Ejecuta con docker-compose up --build 

Advertencia:
El nombre del servicio en `docker-compose.yml` debe ser igual al que le pusiste en la sección `upstream backend_servers`.  