# Uso de while de la forma general
n=0

while n<10:
    print "Hola"
    print n
    n=n+1

print "\nAfuera del while"

# Uso de continue
n = 0

while n<10:
    print "Hola"
    print n
    n=n+1
    if n%2==0:
        continue

    print "Esto solo se imprime a veces"

print "\nAfuera del while"
    

# Uso de break
n = 0

while n<10:
    print "Hola"
    print n
    n=n+1
    if n==5:
        break

    print "Esto solo se imprime mientras esta el ciclo"

print "\nAfuera del while"

# Uso de else
n=0
m=input("Dame un numero ")

while n<10:
    print "Hola"
    print n
    if n==m:
        break

    n=n+1
    print "Sigo imprimiendo"

else:
    print "No encontre el numero"

print "\nAfuera del while"
