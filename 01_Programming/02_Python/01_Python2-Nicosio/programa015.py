# Los tuples son tambien secuencias de objetos, pero inmutables
# Se utilizan () en lugar de []. Si no se usan se toma por defaoul el tuple
# Los elementos se separan por comas, incluso si es solo un elemento
# Son mas rapidos que las listas
# Si la informacion no va a cambiar es la opcion a utilizar
# Se pueden usar como llaves para los diccionarios

# Creacion de un tuple

meses=("Enero","Febrero","Marzo","Abril")
unDato=(5,)

# Acceso al tuple
print meses
print meses[1:3]

for m in meses:
    print m

print meses[2]

# Esto no es vaolido
# meses[1] = "Otro mes"


# Concatenacion
nuevoTuple=meses+unDato

print nuevoTuple

# No se puede borrar un elemento en particular
# pero si el tuple completo
del nuevoTuple
#print nuevoTuple

# Convertir una lista a un tuple
miLista=[":)",":|",":/",":("]
miTuple=tuple(miLista)

print miTuple

# Cvertir un tuple a una lista
miLista2=list(miTuple)
print miLista2

# Operaciones con tuples
#son similares a las de las listas

print len(meses)

otro=(5,6,7)*4
print otro

print 5 in otro
print 9 in otro

tuple1, tuple2, (100,'hola'),(300,'adios')

print cmp(tuple1,tuple2)
print cmp(tuple2,tuple1)
tuple3=tuple2+(50,"saludos")
print cmp(tuple2,tuple3)

print mac(tuple3)
print min(tuple3)

