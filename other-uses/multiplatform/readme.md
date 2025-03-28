arquitectura de pc, mac's servidores es: linux/amd64
arquitectura de IoT, raspberry pi: linux/ard64

comando para crear un docker multiplatafiorma:
docker build --platform=linux/amd64, linux/arm64 -t _image_name_ .

pasos para ejecutar un docker multiplataforma:
1. abre docker desktop > Options > General > use containerd for pulling and storing images.
2. comando para crear un docker multiplatafiorma:
docker build --platform=linux/amd64, linux/arm64 -t _image_name_ .

warning: ejecutar esto va a pesar un montón y no siempre es del todo necesario: