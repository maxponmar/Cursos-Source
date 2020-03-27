
# En este programa hacemos uso del modulo

# Importamos el modulo
#  Directorio actual
#  Variable PYTHONPATH
#  Path de default

import programa023Mod

m=3
n=5

programa023Mod.suma(m,n)
programa023Mod.multi(m,n)

# Importamos solo una funcion del modulo

from programa023Mod import suma

m=3
n=5

suma(m,n)
#multi(m,n)

# Importamos todas las funciones del modulo

from programa023Mod import *

m=3
n=5

suma(m,n)
multi(m,n)

# Imprimimos la variable del modulo
print x

# Variable local y luego la del modulo
x=50
print x
imprime()

# Uso de dir

import programa023Mod

contenidosModulo=dir(programa023Mod)
print contenidosModulo

# Hacemos que se ejecute nuevamente el codigo del modulo
reload(programa023Mod)


# Importamos un paquete
import mensajes
mensajes.hola()
mensajes.como()
mensajes.adios()
