#Configurar un cluster con nginx  

Dockerfile copia el nginx.conf en el contendor para recibir las solicitudes http y distriburilas entre:  
site1, site2 y site3.

y los imágenes deben llamarse 
- "backend1"  
- "backend2"  
- "backend3"  

creas las imagenes como 
- "server1"  
- "server2"  
- "server3"  

La red debe llamarse:  
`backend_servers`

comandos:
`docker network create red_balance`

crea las imágenes:
- docker build -t server1 site1/
- docker build -t server2 site2/
- docker build -t server3 site3/  

crea los contenedores:
- `docker run -d --name backend1 --network red_balance server1`
- `docker run -d --name backend2 --network red_balance server2`
- `docker run -d --name backend3 --network red_balance server3`

# desplega el proxy;
 `docker build -t proxy:1.0 proxy/`  

` docker run --name load-balancer -p 8080:80 --network red_balance proxy:1.0`  

 En un ambiente productivo se hace con algún orquestador.
 