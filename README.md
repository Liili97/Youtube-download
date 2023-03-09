# Script para descargar un video de Youtube

---
#Subir imagen a docker hub
---

Para crear la imagen necesitamos crear el archivo DockerFile, que está mas abajo, y generar una nueva imagen con el, y para ello necesitamos generar una nueva imagen con este comando:

`docker build -t youtubeimage:latest .`

Para subirlo a [DockerHub](https://hub.docker.com/), tenemos que crear un repositorio, con un nombre propio, no tiene que parecerse ni ser igual al de nuestra maquina local. 
Una vez accedemos seleccionamos el nombre de nuestro repositorio vemos como hay una serie de comandos a la derecha que nos indican como subir la imagen.

Pero para subir la imagen tenemos que vincular la terminal a la cuenta, por lo que:

`$ docker login`

`$ docker tag ImagenLocal:VersionLocal nombreusuario:NuevoNombreOnline .`

`$ docker push nombredeusuario/repositorio:version`


Resultado: [Mi imagen](https://hub.docker.com/repository/docker/ecastrofontan/pytube_script/general)

`$ docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3-alpine python hola.py`
-it: interaccion 
--rm: borro el contenedor cuando acabe
-v: volumen  antes de los dos puntos es la ruta ficticia:ruta real de la maquina 
-w: workdir---> ruta


---
#YML
---
```

services:
    python:
        image: youtubeimage:latest
        volumes:
        - ./app:/usr/src/app
        stdin_open: true 
        tty: true
        command: python stats.py
``
---
#DOCKERFILE
---
```
FROM python:3

WORKDIR /usr/src/app

COPY requeriments.txt ./

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

CMD [ "python", "./stats.py" ]

```
