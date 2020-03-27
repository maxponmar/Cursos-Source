# Uso de for para iterar una lista

nombres = ["Susana","Aldo","Nicosio","Ana"]

for nombre in nombres:
    print "Hola ",nombre

# Uso de for con un rango
sumatoria=0

for n in range(10):
    print n
    sumatoria=sumatoria+n

print "La sumatoria es ",sumatoria


# Otro for con rango

for n in range(5,15):
    print n

print "---------"

# Otro for, pero ahora el rango es regresivo

for n in range(15,5,-1):
    print n

# Otro ejemplo de sumatoria

m=input("Dame un numero ")
sumatoria=0

for n in range(1,m+1):
    sumatoria=sumatoria+n
print sumatoria


#Ejmplo con continue

for n in range(10):
    print n
    if n%2==0:
        continue
    print "Hola"

# Ejemplo con break

for n in range(10):
    print n
    if n==5:
        break

print "-------"

# Ejemplo con else

m=input("Dame un numero ")

for n in range(10):
    print n
    if n==m:
        break
else:
    print "Estoy en else"

print "Afuera de for/else"
    


