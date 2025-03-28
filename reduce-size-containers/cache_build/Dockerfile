FROM nginx:1.27.3

# En ningún momento útilice el caché
ARG CACHEBUST = 1

# no siempre es necesario actualizar las librerias del docker
RUN apt-get update && apt-get -y update

# crear un archivo desde el Dockerimage
RUN echo '<html><body><h1>print this crock</h1></body></html>' > /usr/share/nginx/html/index.html



