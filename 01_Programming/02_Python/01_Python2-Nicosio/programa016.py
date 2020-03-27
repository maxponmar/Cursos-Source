# Diccionarios, estructura de datos asociativa no sequencial
# Estructura de datos, tiene una llave y un valor asociado a esa llave
# Las llaves deben de ser inmutables y no es posible tener llaves repetidas
# Los valores pueden ser de cualquir objeto valido en Python
# Solo un valor por llave

# Creaci on del diccionario y acceso

productos={"ft01":"Manzana", "ft02":"Pera","ft03":"Platano","ft04":"Ciruela"}

print productos["ft02"]

print productos

for n in productos:
    print n, productos[n]

#print productos["No existe"]

# Actualizando una entrada

productos["ft03"]="Mango"
print productos

# Adicionando una entrada
productos["ft05"]="Kiwi"
print productos

# Copiamos el diccionario
productos2=productos.copy()
print productos2

# Borrar un elemento
del productos["ft02"]
print productos

# Borrar todos los elementos de la lista
productos.clear()
print productos

# Elimina diccionario
del productos
#print productos
