#Baja la imágen de nginx de docekerhub
FROM nginx:latest

#path del docker para iniciar el html: /usr/share/nginx/html
COPY site/io.html /usr/share/nginx/html

# Para crear la imágen en la terminal: docker build -t ccamsoto/prueba:latest . 

# docker run -it -d --rm -p 8080:80 --name prueba ccamsoto/prueba:latest

# actualizar nombre de imágen: docker image tag prueba:latest ccamsoto/prueba:1.0

# volumen: docker run -it -d --rm -p 8080:80 --name prueba -v ./:/usr/share/nginx/html/nginx ccamsoto/prueba:1.0

VOLUME ["./:/usr/share/nginx/html/nginx"]

#Modifica las ip: docker run -it -d --rm -p 127.0.0.1:8080:80 --name prueba ccamsoto/prueba:1.0

# comprimir: docker export prueba &gt; nginx.tar
# importar: docker import nginx.tar ccamsoto/prueba:latest