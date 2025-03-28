# ¿Cómo creamos un Dockerfile seguro?  

Para solidificar la seguridad en tus imágenes Docker, es esencial modificar tu Dockerfile adecuadamente.

Usar una imagen base: Usualmente, empezamos con una imagen base como Nginx. Puedes hacer esto con el siguiente comando:  

`FROM nginx`

Crear grupos y usuarios: Define un grupo y un usuario con el mismo nombre por conveniencia y claridad.  

`RUN groupadd amin && useradd -g amin amin`

Asignar permisos de acceso limitados: Especifica las carpetas a las que el nuevo usuario puede acceder.  

`RUN chown -R amin:amin /var/www/html`  

Cambiar al usuario no-root: Antes de ejecutar otras tareas, asegúrate de cambiar al nuevo usuario.  

`USER amin`  

Ajustar comandos según privilegios: Asegúrate de que cualquier comando que necesite derechos de root se ejecute antes de cambiar al usuario.  
  
```bash
#Commands needing root access
RUN apt-get update && apt-get install -y some-package
```

Luego puedes crear el usuario y cambiar a él como se mostró anteriormente.