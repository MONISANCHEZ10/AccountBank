### CASO PRACTICO USO ZODB

## Requisitos 
- Instalacion depython en su version 2.7 o superior
- Instalacion de ZoDB ``pip install ZODB``.

## Ejecucion 

- Listar cuentas existentes:
```
$python accountBank.py 
```

- Añadir cuentas nuevas:

```
$ python accountBank.py -add "Juan Perez" "004" "BCN" "234 343" "0000004"

```

- ELiminar cuentas por id:
```
python accountBank.py -delete "0000004"
```

