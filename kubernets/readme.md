# guía para configurar kubernets por primera vez:
A pesar de mi límitado hardware, aquí confuguro el kubernets:
## Pasos de instalación
Disclaimer: no necesitas de un cluster, kubernets ya viene instalado en docker desktop.

1. instala: abre docker desktop > settings > kubernets > enable kubernets > apply and restart > cuando haya terminado la instalación: reset kubernetes cluster.

2. abre la terminal, en el directorio que quieres hacer la instalación e instala **kubectl**, la CLI que te permitirá interactuar con el clúster de Kubernetes:  

`curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"`

3. Instala un fichero al cual hay que darle permisos de administrador: `chmod +x kubectl`

4. Mueve el fichero al directorio de ejecutables para poder acceder desde cualquier lugar:

`sudo mv kubectl /usr/local/bin/` 

5. Para validar la correcta instalación ejecuta: `kubectl version --client`  

## Enlazar mi cluster de kubernetes dentro de mi docker terminal:

1. Valida que el enlace es correcto: `kubectl config get-contexts`. Si lista a docker-desktop funcionó.

2. Si ejecutas `kubectl get nodes`, tu pc se listará como un nodo.