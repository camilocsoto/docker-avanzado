# Integración continua
Mediante github actions automatiza la actualización de imágenes de dockerfile.  

Para hacerlo sigue estos pasos:
1. Crea el dockerhub en el repo que necesitas  
2. haz el push al repo
3. Seleccionas la categoría de "actions"
4. Seleccionas "set up a workflow yourself"
5. Debes crear un docker.yml:
```bash
name: Docker Image CI # Define el nombre del flujo de trabajo en GitHub Actions.

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ] #Especifica cuándo se ejecutará este workflow: Cuando haya un push o un PR a la rama main.

jobs:
  build: #Define un job llamado build, que ejecutará unos pasos para construir y subir la imagen Docker.
    name: Docker build # Nombre del job dentro del workflow.
    runs-on: ubuntu-latest # Especifica el sistema operativo en el que se ejecutará el job
    steps: # Cada paso es una acción que se ejecutará secuencialmente.
      - name: Checkout the repo
        uses: actions/checkout@v3 # clona el código del repositorio dentro del entorno de ejecución.
      - name: Build the Docker image
        uses: docker/login-action@v2 #  inicia sesión en Docker Hub.
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }} # variables de entorno secretas configuradas en GitHub
      - name: Build the Docker image # Construir la imagen Docker:
        run: docker build  --platform linux --tag ${{ secrets.DOCKERHUB_USERNAME }}/backenddockerci:latest -f ci/dockerfile .
      - name: Push the Docker image
        run: docker push ${{ secrets.DOCKERHUB_USERNAME }}/backenddockerci:latest #Subir la imagen a Docker Hub
```
Igual se puede encontrar en el repositorio del profesor
<https://github.com/platzi/docker-avanzado/tree/main/.github/workflows>  

6. Antes de crear el main.yml debes crear las variables de entorno en github:
6.1 en settings > secrets and variables > actions > repository secret
6.2 debes poner el mismo nombre del yml: `DOCKERHUB_USERNAME` y en sencret le pones tu usuario de dockerhub. Lo creas.
6.3 Añade el token de acceso: En dockerhub, account settings > personal access token > generate new token > asigna nombre > dale los permisos r, w, d y generate.
6.4 copia el token y pegalo en la variable `DOCKERHUB_TOKEN`
7. Ya puedes automatizar que los docker se suban solos tras hacer push


##warnings:
los secretos deben estar escritos en mayuscula