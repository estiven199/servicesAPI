# SERVICES API

## Descripción

API para explorar los distintos servicios que ofrecen nuestros Freelancers y como están conformados cada uno de ellos.

## Índice 

- [Preparacion](#preparacion)
- [Instalación](#instalación)
- [Uso](#uso)

## Preparacion

- Instalar Docker y Docker Compose en su sistema local siguiendo las instrucciones proporcionadas en la   [documentación oficial de Docker ](https://docs.docker.com/)


## Instalación

-Clonar el proyecto en la maquina localmente. [Clonar un repositorio ](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository)

Ejecute los siguiente comandos:

```sh
docker compose build "Construye las imágenes de Docker que se especifican en el archivo docker-compose.yml"
docker compose up  "Crea y ejecuta los contenedores de un proyecto a partir de las imágenes de Docker"
```
El archivo docker-compose.yml especifica tres contenedores: un contenedor api, postgres y pgadmin.

El contenedor api se construye a partir del directorio actual (.) y se le da el nombre de servicesAPI. Está configurado para reiniciar siempre y expone el puerto 8000 en la máquina anfitriona, mapeándolo al puerto 8000 en el contenedor. El contenedor api también está vinculado al contenedor mongo y tiene un volumen que mapea el directorio actual en la máquina anfitriona a /usr/src/app en el contenedor.

El contenedor postgres se basa en la imagen postgres y se le da el nombre de postgres. Expone el puerto 5432 en la máquina anfitriona, mapeándolo al puerto 5432 en el contenedor.

 # volumes:
```sh - ./initdb.sql:/docker-entrypoint-initdb.d/initdb.sql ```
Esta linea crea las bases de datos para pruebas. Si necesita crear estas tablas para pruebas, recuerda activar la linea antes de ejecutar los comandos anteriores.


 [documentación oficial de la API ](http://localhost:8000/docs)