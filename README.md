
# Desempleo en Barcelona

https://as01.epimg.net/diarioas/imagenes/2022/04/30/actualidad/1651323395_313362_1651323476_noticia_normal_recorte1.jpg

Podremos ver el desempleo en Barcelona entre los años 2013 y 2017 ambos incluidos.

Además, tendremos la posibiliad de seleccionar entre varias opciones para filtrar los resultados de desempleo entre los años mencionados por algunos parámetros a escoger, tales como distrito, barrio, género, año y mes.


## Referencias API

#### Desempleo por año

```
  GET /year/all
```
Podemos ver el desempleo total del año seleccionado. 

#### Filtrado por año, mes, distrito, barrio y género

```
  GET /desempleo
```
Podemos filtrar de una forma más concreta, escogiendo entre los parámetros arriba mencionados.

#### Retorna los distintos meses de toda la colección

```
  GET /month/all
```
Podemos ver la diferencia de desempleo entre los distintos meses.


#### Retorna los distintos distritos de toda la colección

```
  GET /district/all
```
Podemos filtrar el desempleo según el ditrito deseado.

#### Retorna los distintos barrios de toda la colección

```
  GET /barrio/all
```
Además del distrito, podemos acotar un poco más en el filtrado del desempleo y seleccionar por barrio.

### Retorna los distintos géneros de toda la colección

```
  GET /gender/all
```
En este caso, será posible buscar y comparar el desempleo en función del género.

#### Retorna el estado de desempleo

```
  GET /status/all
```
Este filtro nos permitirá ver el estado de desempleo, midiendo así la cantidad de personas cuya situación es "Demand_occupation" o "Registered unemployed"


## Authors

- [@SoniaSancho84](https://github.com/SoniaSancho84/MidProject_Barcelona)