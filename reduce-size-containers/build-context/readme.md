# Build context y reducción de transferencias
El Docker solo tiene acceso a la carpeta src y no a este readme.md:

con acceso al readme.md y al src:  
./../`docker build -t app build-context/`


El comando `EXPOSE` es solo informativo, mientras que `-p` o `--publish` ya son para acceder directamente al docker