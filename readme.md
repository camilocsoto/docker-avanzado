# Pasos para reducir el tamaño de una imágen y un docker:
1. Crea un Dockerfile multi-stage
2. No guardes caché de las instalaciones, hace más pesado el docker.
hazlo con `docker build --no-cache -t tag_version`   o `ARG CACHEBUST = 1`
3. Si actualizas tu docker, debes borrar los ejecutables con este comando:
`rm -rf /var/lib/apt/lists/*`
4. Utiliza los archivos .dockerignore
5. No uses capas innecesariamente.


1. imágenes Docker oficiales  

2. considerar una versión a la etiqueta 

3. elegir imágenes mínimas con Alpine

4. usa Multi Stage Builds

5. Borra el cache del docker desktop

6. Crea usuarios dentro del dockerfile


not use distroless:
When you aren’t running statically compiled binaries in a container


It's fairly simple. If your application requires an external runtime and/or packages from a distro, distroless is not a good base. If your application is self-contained and only needs a few files in place, it is a good base. 

I’ve never used them, but off the top of my head:

Pro: minimal and near zero attack surface

Con: literally zero debugging tools.

If you have everyone build off the same distro (say, everyone builds off Ubuntu:24.01) then space savings aren’t the biggest since you have common layers.
