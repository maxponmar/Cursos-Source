# Shallow copy y deep copy, superficial y profunda
# Solo es importante para los objetos compuestos
"""
# esto no es una copia solo se referencia a la mima instancia que A
a=5
b=a

nombres1=["Nicosio","Susana"]
nombres2=nombres1

# ambos a la misma intancia
print "nombres1",nombres1
print "nombres2",nombres2

# Al modificar nombres2, tambien se modifica nombres1 ya que esta referenciada a esa instancia
nombres2[1]="Aldo"
print "nombres1",nombres1
print "---------------"

# nombres2 ahora apunta a otra instancia
nombres2=["Ana","Luis"]
print "nombres1",nombres1
print "nombres2",nombres2

print "---------------"
"""
# Copia con slice de un objeto que no es compuesto
# parece que no tenemos el problema anterior

letras1=["a","e","i","o","u"]
letras2=letras1[:]

print "letras1",letras1
print "letras2",letras2
print "--- Se hace cambio ---"
#Cambiamos algo en letras2
letras2[1]="z"
print "letras1",letras1
print "letras2",letras2

print "----------------------"

# Copia con slice de un objeto que es compuesto
# Nuevamente tenemos las referencias

fonemas1=["a","e","i",["ba","be","bi"]]
fonemas2=fonemas1[:]

print "fonemas1", fonemas1
print "fonemas2", fonemas2
# Aqui no hay problema
fonemas2[1]="u"
print "fonemas1", fonemas1
print "fonemas2", fonemas2

# Aqui si
fonemas2[3][0]="DA"
print "fonemas1", fonemas1
print "fonemas2", fonemas2
print "----------------------"


# Para solucionar hacemos una copia profunda
# Necesitamos usar el modulo copy
from copy import deepcopy

fonemas1=["a","e","i",["ba","be","bi"]]
fonemas2=deepcopy(fonemas1)

# No hay problema en este
fonemas2[1]="u"
print "fonemas1", fonemas1
print "fonemas2", fonemas2
print "----------------------"
# Y ya no hay problema con este tampoco
fonemas2[3][0]="DA"
print "fonemas1", fonemas1
print "fonemas2", fonemas2

