apt upgrade se puso a propósito para que la construcción del docker sea más lenta.

El primer build va a ser lento (11.2)
El segundo va a ser rápido (2.4)
Esto se debe gracias al caché:

 => CACHED [2/3] RUN apt-get update && apt-get -y update
 => CACHED [3/3] RUN echo '<html><body><h1>print this crock</h1></body></html>' > /usr/share/nginx/html/index.html   

Esto hace la imágen más pesada. Para evitar que tenga caché utiliza el comando:  
`ARG CACHEBUST = 1`  
De este modo, el contenedor deja de pesar tanto. O puedes utilizar este:  
`docker build --no-cache -t tag_version`  
