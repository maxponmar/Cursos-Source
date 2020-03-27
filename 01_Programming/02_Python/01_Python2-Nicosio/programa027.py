# Comprension de listas
# Implementa en las listas la notacion de los conjuntos que usal los matematicos

valores=[1,2,3,4,5]

cuadrados=[(x*x) for x in valores]
print cuadrados

# TCP
trinomios=[(x*x+2*x*y+y*y) for x in range(1,3) for y in range(1,3)]
print trinomios

# Convertir de pulgadas a centimetros, solo para  valores positivos
pulgadas=[1,3.5,-6,-6,5.1,-3.2]

cm=[(x*2.54) for x in pulgadas if x>0]
print cm

# Comprension de Generator, crea un generador en lugar de una lista
# funcion que trabaja como un iterador

valores=[1,2,3,4,5]
gen1=(x*x for x in valores)
print gen1

# Convertimos a lista
gen2=list(gen1)
print gen2

# Comprension de sets
valores=[1,2,3,4,5,4,5]
cuadrados={x*x for x in valores}
print cuadrados
