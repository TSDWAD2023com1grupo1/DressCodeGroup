# DRESSCODE | BACKEND

DJANGO VERSION
4.2.13

PYTHON VERSION
3.8.0

___

## Scripts MYSQL
----Crear la estrutura de la base de datos-----

La base de datos dresscode_2 puede generarse con el script "Script CREAR tablas DB dresscode_2".
En caso de error se pueden generar tabla por tabla, desde arriba hacia abajo, una a una.


----Insertar datos en la DB-----

El INSERT para llenar la base de datos se realiza con el script  "Script INSERT llenar datos en la DB dresscode_2".
Tiene alrededor de 4 campos completos por tabla, y la totalidad de los productos de la tienda, con sus imagenes como urls.


----EXPORT DE LA BASE CON LOS DATOS-----
Se realizo un EXPORT con MySQL Workbench de la estructura y los datos de toda la BD funcionando hasta el momento.
Todos los scripts de cada tabla estan en la carpeta DATA EXPORT.

## Requerimientos
#### asgiref==3.8.1
#### backports.zoneinfo==0.2.1
#### Django==4.2.13
#### django-cors-headers==4.3.1
#### djangorestframework==3.15.1
#### mysqlclient==2.2.4
#### sqlparse==0.5.0
#### typing-extensions==4.12.0
#### tzdata==2024.1


## Rutas de la API

  #### "usuarios" api/v1usuarios/
  ####  "productos"/api/v1productos/
  ####  "carritos" /api/v1carritos/
  ####  "envios": /api/v1envios/
  ####  "pedidos" /api/v1pedidos/
  ####  "articulos_pedido" /api/v1articulos_pedido/
  ####  "pagos" /api/v1pagos/


