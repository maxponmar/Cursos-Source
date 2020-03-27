# Creacion de listas

frutas = ["pera", "manzana","ciruela","platano"]
califs= [8,7,10,9,8]
varios = ["internet",14.5,"estrella",5,True]

for elemento in frutas:
    print elemento

print ("--------")

for elemento in califs:
    print elemento

print ("--------")

for elemento in varios:
    print elemento

print ("--------")

# Acceder a la lista por indice

print frutas[0]
print frutas[2]
print frutas[-1]
#print frutas[7]

# Actualizar un valor de la lisa

print "="*10

print "Original"

for elemento in frutas:
    print elemento

print "-"*10

frutas[2] = "albaricoque"

for elemento in frutas:
    print elemento

print "-"*10

# Borrando un elemento

del frutas[2]

for elemento in frutas:
    print elemento

print frutas[2]

print "---------"

#############

# Operaciones y funciones sobre listas

# Longitud
print len(frutas)
print "---------"
# Concatenacion
lista2 = califs+varios

for elemento in lista2:
    print elemento

print "------"

# imprimire lista completa sin usar for
print califs
print varios
print lista2
print "---------"
# Membresia

print 7 in lista2
print "manzana" in lista2
print "---------"

# Repeticion

lista3 = frutas*2

print lista3
print"---------"

# Slicing

lista4 = lista2[:5]

print lista2
print lista4
print "------"
