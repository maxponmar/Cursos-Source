# Paso por copia con objeto inmutable

def mostrar(a):
    print "  ID objeto ", id(a), " valor objeto ", a
    a=100
    print "  ID objeto ", id(a), " valor objeto ", a

numero=5
print "Antes ",numero
mostrar(numero)
print "Desde fuera ", numero
print "------------------"

# Paso por referencia de objeto mutable
def mostrarLista(lista):
    print "  ID objeto ", id(lista), " valor objeto ", lista
    lista=["Hola"," a todos"]
    print "  ID objeto ", id(lista), " valor objeto ", lista

def mostrarLista2(lista):
    print "  ID objeto ", id(lista), " valor objeto ", lista
    lista+=["Hola"," a todos"]
    print "  ID objeto ", id(lista), " valor objeto ", lista

palabras=["pizza","auto","programacion"]
print "Antes ",palabras
mostrarLista(palabras)
print "Desde fuera ", palabras

print "=== Ahora actua como referencia"
print " Antes ", palabras
mostrarLista2(palabras)
print " Desde fuera ", palabras

print "=== Ahora actua como referencia pero con copia superficial"
palabras=["pizza","auto","programacion"]
print "Antes ", palabras, id(palabras)
mostrarLista2(palabras[:])
print "Desde fuera ", palabras
