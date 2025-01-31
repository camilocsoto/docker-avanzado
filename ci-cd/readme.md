# GitHub Actions 
## CI: Integración continua [docker.yml]
Mediante github actions automatiza la **subida** de imágenes de dockerfile.  

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
        run: docker build  --platform linux --tag ccamsoto/ci:latest -f ci/dockerfile .
      - name: Push the Docker image
        run: docker push ccamsoto/ci:latest #Subir la imagen a Docker Hub
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

## CI: Validación de docker a subir:  [testing.yml]
Se generan pruebas a un docker generico de alpine, entrando a directorios y creando archivos.  
```bash
name: Docker Test

on:
  push:
    branches:
      - main
      
jobs:
  docker-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Run Docker container
        run: |
          docker run -d --name testcontainer alpine tail -f /dev/null

      - name: Run tests
        run: |
          docker exec testcontainer /bin/sh -c "
            echo 'Ejecutando pruebas...';
            cd home
            mkdir amin 
            cd amin
            printf 'Este es el contenido del archivo.\nPuede incluir varias líneas.\n' > ejemplo.txt
            ls -a || exit 1
          "
```
## CD: Despliega una web app de azure automáticamente [docker.yml]
Este paso es el de despliegue continuo para publicar en azure.

1. En azure, en el grupo de trabajo crea una web app.
2.1 Asignale la group base, name, plan basic, salta el paso de bases de datos. 
2.2 Indica el origen, image and tag `ccamsoto/ci:latest`. No es necesario indicarle un stratup command
2.3 habiltia "enable public access" a pesar de que no sea un endpoint, y deja deshabilitado injección de redes
2.4 Cuando tu recurso se haya creado
3. En overview, busca settings > configuration > habilita SCM Basic Auth Publishing y FTP basic Auth Publishing Credentials
4. En deployment center >source debe estar seleccionado "container registry", en continuous deployment, selecciona "on" y guarda los cambios
5. En deploy center, selecciona manege public profile y descarga el archivo xml.
6. Crea la variable de entorno en repo > settings > Secrets and variables, allí debes crear una acción `AZURE_WEBAPP_PUBLISH_PROFILE ` y pegas el archivo .xml
7. Edita el archivo docker.yml. y al final agrega un nuevo paso:


```bash
name: Docker Image CI

on:
  push:
    ...
runs-on: ubuntu-latest # Especifica el sistema operativo en el que se ejecutará el job
    steps: # Cada paso es una acción que se ejecutará secuencialmente.
      - name: Checkout the repo
      ...
      - name: App service auth
        uses: azure/webapps-deploy@v2
        with:
          app-name: 'camilocsoto'
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          images: 'ccamsoto/ci:latest'
    
```