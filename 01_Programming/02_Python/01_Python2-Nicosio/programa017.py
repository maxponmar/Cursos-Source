# Operaciones y funciones con el diccionario

productos={"ft01":"Manzana", "ft02":"Pera","ft03":"Platano","ft04":"Ciruela"}
productos2={"ft01":"Manzana", "ft02":"Chabacano","ft03":"Platano","ft04":"Ciruela"}
productos3={"ft01":"Manzana", "ft02":"Pera","ft03":"Platano","ft04":"Ciruela"}

# Comparacion

print cmp(productos, productos2)
print cmp(productos, productos3)
print cmp(productos2, productos)

# Longitud
print len(productos)

# Conversion a cadena

cadena = str(productos)
cadena2 = "->"+cadena+"<-"
print cadena2

# Conocer si existe una llave

print productos.has_key("ft02")
print productos.has_key("NoExiste")

# Lista de pares (Llave, valor) como tuples adentro de una lista
print productos.items()

# Lista de llaves en el diccionario
print productos.keys()

# Lista los valores en el diccionario
print productos.values()

# Set defaoult, se usa como get, pero damos un valor a colocar
# default si la llave no existe
print productos.setdefault("ft02","No hay")
print productos.setdefault("No existe","No hay")

print productos

# Otra forma de adicionar una entrada con update
productos.update({"ft07":"Albaricoque"})
print productos
