# Definicion de funciones

def mostrar(numero):
    "Esta funcion imprime el numero"
    print numero

# Aqui el codigo principal
mostrar(1)
mostrar(3)
mostrar(5)
print "------------"

# Aqui vemos el uso de Docstring
def mostrar(numero):
    "Esta funcion imprime el numero"
    print numero
print mostrar.__doc__
print "------------"

# Este ejemplo muestra como pasar parametros
def adicionar(nombre):
    nombre="Hola "+nombre
    print nombre

def mostrarSuma(a,b):
    r=a+b
    print r

adicionar("Maximiliano")
nombre="Luis"
adicionar(nombre)
mostrarSuma(5,4)
print "------------"


# En este ejemplo usamos parametros opcionales

def multi(a, b=5):
    r=a*b
    print r

# invocamos normal
multi(4,8)
# invocamos con un solo parametro
multi(7)
print "------------"


# Aqui usamos keyword para pasar los parametros
def muestraValores(a=1,b=2,c=3):
    print "A es ",a
    print "B es ",b
    print "C es ",c
    print "------------"

# invocamos normal
muestraValores(5,10,15)
# invocamos con keyword
muestraValores(b=6,c=8,a=16)
# invocamos con keyword y parametro opcional
muestraValores(b=20)
print "------------"

# Numero arbitrario de parametros
def sumatoria(a,*mas):
    sum=a;
    if len(mas)>0:
        for n in mas:
            sum=sum+n
    print sum

sumatoria(5)
sumatoria(5,3,1)
sumatoria(1,2,3,4,5)
print "------------"

# Uso de return
def suma(a,b):
    r=a+b
    return r
s=suma(5,4)
print s
s=suma("Hola", " a todos")
print s
print "------------"

# Variables globales y locales
g=5

def funcion(mensaje):
    local=3
    print mensaje*3
    print local
    print "bye "*g
funcion("Hola ")
print g
#print local
print "------------"

def adicionar(nombre):
    nombre="Hola "+nombre
    print "En adicionar ",nombre

def mostrarSuma(a,b):
    r=a+b
    print "En mostrarSuma ",nombre
    print r

adicionar("Nicosio")
nombre="Luis"
adicionar(nombre)
mostrarSuma(1,2)
print "En principal ",nombre
print "------------"
