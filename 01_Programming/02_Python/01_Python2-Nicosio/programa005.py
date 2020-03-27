# Variables
# Python es OO y no es necesario declarar las variables antes de usarla
# Soporta tres clases de numeros: enteros, flotantes y complejos

# Definimos un entero. El operatdor = es de asigancion
valor=5
print valor

# Definimos un flotante
precio = 18.5
print precio

# Lo definimos con constructor
saldo=float(14)
print saldo

# Podemos definir discretamente al hacer operacion
total = precio + saldo
print total

# Se pueden tener variables de tipo string
nombre = "Aldo"
print nombre

# Y tambien de tipo bool
acierto = True
print acierto

# Se pueden hacer asignaciones multiples
calif1, calif2 = 10,8
print calif1
print calif2

print "-"*20

#Diferentes formas en las que podemos usar print

#Podemos hacer este tipo de impresiontes
print "El alumno uno tiene la calif de ", calif1, "y el dos de", calif2

# Tambien de esta forma con el uso de formateadores
print "El primer alumno tiene la calif de %d y el segundo de %d" %(calif1, calif2)
print "%s el precio es de %f por articulo" %(nombre, precio)
print "El precio es de %.2f pesos" %precio

#Creacion de una cadena con formato
formato = "Una variable %r, otra variable %r"
print formato %(precio, saldo)
print formato %(nombre, acierto)
print formato %(valor, calif1)

# Imprimir multiples lineas a la vez

print """
Aqui vamos a imprimir
multiples lineas
a la vez.
Pthon lo permite
"""

# Python tambien tiene codigos de escape
print "Voy a imprimir una \\ aqui"
print "Si lo deseo pongo \' o \" en la impresion"
print "Una linea \notra linea abajo"
print "\t con salto de tab"


