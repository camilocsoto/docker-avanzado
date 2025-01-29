DEBES IR A downloads/u/azure/primer_docker/ aquí se ejecuta todo.

# Guía para Configurar Azure y Subir una Imagen de Docker  

Debes entender que tienes tu imágen en un contenedor privado. Sin embargo, no significa que no sea accesible.  

## Disclaimer  
Creé una cuenta de Azure utilizando mi correo universitario y (opcionalmente) seleccioné el plan de **Azure for Students**. Esto puede variar según tu suscripción.  

---

## 1. Crear un Grupo de Recursos  

1. En el menú lateral izquierdo, selecciona **"Crear un recurso"**.  
2. En la barra de búsqueda, escribe **"Grupo de recursos"**.  
3. Selecciona la primera opción:  
   ![*(Inserta una imagen aquí si es necesario)*  ](https://static.platzi.com/media/user_upload/Sin%20título-c702935f-7306-4b08-b7bf-4cb4ba47ef2d.jpg)
4. Configura el grupo de recursos:  
   - **Suscripción:** Selecciona tu suscripción (puede no funcionar con cuentas gratuitas, no lo probé).  
   - **Nombre del grupo de recursos:** Por ejemplo, "contenedoresPlatzi" (este nombre no se podrá cambiar después).  
   - **Región:** Selecciona la región donde se desplegará tu servicio. Yo elegí **Brazil South** (Sudamérica).  
5. Haz clic en **Siguiente: Etiquetas**, asigna un nombre y un valor (por ejemplo: `ambiente: devOps`), y luego selecciona **Siguiente**.  
6. Por último, haz clic en **Crear**.  

---

## 2. Crear un Registro de Contenedores en Azure  

1. En tu **Grupo de Recursos**, haz clic en **Crear** y selecciona **Container Registry**.  
2. Los campos principales ya estarán preconfigurados por el Grupo de Recursos. Solo necesitas:  
   - Asignarle un nombre.  
   - Hacer clic en **Crear**.  
3. ¡Listo! Registro creado exitosamente.  
   *(Inserta una imagen aquí si es necesario)*  

---

## 3. Subir una Imagen de Docker al Repositorio  

### Advertencias  
- **Instalar Azure CLI:**  
  - Si tu PC no reconoce el comando `az --version`, instala Azure CLI:  
    - [Instrucciones para Windows](https://learn.microsoft.com/es-es/cli/azure/install-azure-cli-windows?tabs=azure-cli)  
    - [Instrucciones para WSL2/Linux](https://learn.microsoft.com/es-es/cli/azure/install-azure-cli-linux?tabs=apt)  
- **Docker Desktop:** Asegúrate de que Docker Desktop o el daemon de Docker estén activados.  
- **Iniciar sesión en Azure CLI:** Ejecuta `az login` para iniciar sesión en tu cuenta de Azure (esto abrirá una ventana en el navegador).  

### Pasos  
1. Ve a la sección **Overview** de tu registro de contenedores y copia el **Login Server** (sin incluir `.azurecr.io`).  
2. Ejecuta el comando:  
   ```bash
   az acr login -n primerdocker
    ```
3. Con esto, ya tienes acceso al registro de contenedores en Azure.  
  
---
  
## 4. Crear y subir tu dockerfile  

1. Descarga la carpeta y el Dockerfile del curso Docker: Fundamentos, clase 6 (revisa los recursos de la clase).  
   ```bash
   docker build -t primerdocker.azurecr.io/sitioweb:latest .
    ```
2. Ejecuta el siguiente comando para construir la imagen:  
    ```bash
   docker push primerdocker.azurecr.io/sitioweb:latest
    ```  

---
  
## 5. Crear llaves de acceso para el administrador.  

1. En el grupo de recursos, debes ir a settings > acces keys  

2. Regresa a grupo de recursos e instala docker container app para desplegar la app.  

## 6. Crear el contenedor de despliegue!  

1. Dale un nombre al app container.  

2. En `origen de la implementación` debes elegir images, porque no tienes un artefacto.  

3. Creas un nuevo entorno de apps contenidas.  

4. Al dar siguiente, estableces la imágen dentro de la app.

https://tinypic.host/images/2025/01/28/Sin-titulo.png  

5. Habilita la entrada de tráfico y seleccionas `aceptar tráfico desde cualquier lugar.` y le das a todo next.

6. Una vez desplegada, en `application > containers`: quedará la info de la imágen



# Links de ayuda
- [Crear grupo de recursos en Azure](https://www.youtube.com/watch?v=aPDMRTPPkiA)  