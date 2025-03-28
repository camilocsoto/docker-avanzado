Cuando construyas el dockerfile lo ejecutas para crear la imágen:
`docker build -t _name_ .`
Antes de crear el contenedor a partir de la imágen, debes crear el `dockerignore`, y ahora sí:
`docker run -it --rm _name_`
con `--rm` solo borras las versiones anteriores de dockers.