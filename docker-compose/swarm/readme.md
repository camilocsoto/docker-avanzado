# docker swarm  

Es un miniorquestador, en este caso es un stack de dockerfiles: si se cae uno, y no se recupera, en 10 seg se crea:

## ¿cómo ejecutarlo?
1. Corre la imágen de `/app` que creará el nginx: `docker build -t ccamsoto/swarm:latest .`

2. En vsc, creas el `docker-compose.yml`:  

```bash 
services:
  web:
    image: nginx:latest 
    ports:
      - "80:80"
    deploy: # inicia docker swarm, especificamente sus services.
      replicas: 3 # tiene 3 repos en paralelo
      update_config:
        parallelism: 1 
        delay: 10s
      restart_policy:
        condition: on-failure # si se cae la imágen de la replica y no se recupera en 10 seg: corre una nueva imágen
    networks:
      - frontend

  app:
    image: ccamsoto/swarm:latest # debes trabajar con imagenes, no dockerfiles.
    deploy:
      replicas: 5
      restart_policy:
        condition: any # cualquier fallo reincia la imágen.
    networks:
      - frontend
      - backend

networks:
  frontend:
    driver: overlay
  backend:
    driver: overlay # definida por defecto en un orquestador.
```

3. Ejecuta `docker swarm init`  

4. Corre el siguiente comando: `docker stack deploy -c docker-compose.yml deploy_swarm #-c indica compose`  

5. Si eliminas un contenedor / instancia, se crea otra vez

## Para validar la creación de las instancias

1. corre el comando `docker stack ls` y te mostrará todos los servicios activos.  

2. corre el comando `docker stack rm deploy_swarm` para eliminar todo

3. para borrar todo: `docker swarm leave --force` 