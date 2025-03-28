#Esto se saca de las etiquetas de las imágenes de docker CLI
FROM python:3.12-alpine3.17
# Directorio del docker donde se van a instanciar los docker, por convención es /app
WORKDIR /app
# Copiar el archivo requirements.txt para instalar las dependencias
COPY requirements.txt /app
RUN pip install -r requirements.txt 
# Mover todo el código de aquí al docker
COPY . .
# Ejecutar un comando en la terminal de docker
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]

#CON ESTO CREAS LA IMÁGEN