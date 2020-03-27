# Operadores booleanos

a=input("Dame un numero ")

if a>=5 and a<=10:
    print a," esta entre 5 y 10"

b= input("Dame un numero que divida exactamente a 8 ")

if b==1 or b==2 or b==4 or b==8:
    print "Correcto"
else:
    print "Incorrecto"

if not(b==1):
    print "El uno divide a todos exactamente"
