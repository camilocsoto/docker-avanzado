# crea archivos .sh para que sea más legible:
1. Deja toda la configuración e instalación en el dockerfile antes de desplegar el contenedor.
2. De este modo, ya todo estaría funcionando en el server y no se sobrecargaría.

## Óptimizar dockerfile
1. Crea un archivo .sh y lo indicas en una capa COPY para mandarlo a la imágen.
2. crea una capa RUN para darle permisos con chmod al .sh
3. Crea una capa RUN para ejecutar el .sh 
pdt: revisa los comandos en el dockerfile.


# Corre la imágen y el docker:

docker build -t script .  

docker run --name scripts script

warning: se cierra al hacer esto porque no hay nada ejecutándose que lo mantenga arriba:

Para evitar eso, ejecuta:

docker run -d --name scripts script tail -f /dev/null
tail -f: docker espera alguna interacción y se mantiene arriba. 

docker exec -it script ash -c "
echo 'puedes ejecutar:';
apk update;
apk upgrade;
echo 'done'
"
