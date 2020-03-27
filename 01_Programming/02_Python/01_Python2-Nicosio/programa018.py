# Conjuntos - Sets
# Es una coleccion no ordenada de objetos unicos e inmutables
# Trata de ser similar a los conjuntos en el sentido matematico

# Creacion de sets usando set, tambien se puede usar {} en algunas versiones de Python

letras=set("Hola a todos")
print letras

meses=set(["enero","febrero","marzo","abril"])

print meses

numeros=set((1,3,5,7,9,3,10))

print numeros

# Inmutables
#inmutable=set(([1,2,3],[4,5,6]))

# No puede contener objetos mutables pero si es mutable

# Adicion al set
meses.add("mayo")
print meses

# Los frozensets son similares pero inmutables

dias=frozenset(["lunes","martes","miercoles"])
#dias.add("jueves")
print dias
