# Pedir informacion al usuario
# usando input
# al escribir cadenas hay que ponerlas con ""

nombre = input("Dame tu nombre ")
base = input("Dame la base ")
altura = input("Dame la altura ")
area = base * altura
perimetro = 2 * (base + altura)

print "Hola ", nombre," el area es ", area," y el permietro es ", perimetro

# Usando raw_input

nombre = str(raw_input("Dame tu nombre "))
base = float(raw_input("Dame la base "))
altura =    float(raw_input("Dame la altura "))
area = base * altura
perimetro = 2 * (base + altura)

print "Hola ", nombre," el area es ", area," y el permietro es ", perimetro

# Comparando entradas con input y raw_input
print "Con input"
a=input("un valor ")
print (a,type(a))

print "Ahora raw input"
b = raw_input("mismo valor ")
print (b,type(b))



               
