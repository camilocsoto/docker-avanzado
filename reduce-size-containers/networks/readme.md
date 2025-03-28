¿Qué modelos de red existen en Docker?

modelo de red bridge

modelo de host

modelo de red aislado

modelo overlay

modelo MacVLAN

1. Crea una red docker network create mi_bridge

2. docker run -d `--network mi_bridge` --name servidor_web nginx:latest
- d: segundo plano
3. Crea otro para permitir info: docker run -it `--network mi_bridge` --name cliente alpine ash
-it: interactiva

4. curl http://servidor_web