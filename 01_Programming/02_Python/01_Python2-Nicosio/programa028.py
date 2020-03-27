# Manejo avanzado de funciones y Decoradores
# Es un objeto que puede ser invocado y que modifica una funcion o clase

# En Python los nombres de las funciones son referencias y una funcion
# puede tener mas de un nombre

def cuadrado(a):
    r=a*a
    return r

potencia2=cuadrado

print cuadrado(2)
print potencia2(4)

# Si tenemos dos o mas referencias, podemos eliminar una sin perder la otra

del cuadrado
print potencia2(5)

# En Python se puede definir una funcion adentro de otra

def cuadradoPar(a):

    def checarPar(x):
        return x%2==0

    if(checarPar(a)):
        print "Se puede hacer el cuadrado"
        return a*a
    else:
        print "No se puede hacer el cuadrado"
        return 0

print cuadradoPar(16)
print cuadradoPar(15)

# En Python la funcion es un objeto y cualquier objeto puede ser pasado
# como parametro, por lo que las funciones pueden ser pasadas como parametro

def parImpar(a):
    if(a%2==0):
        print "Es par"
    else:
        print "Es impar"

def ImprimeMucho(a):
    valor=str(a)
    print (valor+" - ")*a

def potencia(func,x):
    r=x**x
    func(r)
    print "La potencia es", r

potencia(parImpar,5)
potencia(ImprimeMucho,4)

# Las funciones tambien pueden regresar funciones

def f(x):

    def g(y):
        print "estoy en g, este es x:",x," este es y", y
        return y + x
    print "estoy en f, este es x:", x
    return g

nf1=f(1)
nf2=f(3)

print(nf1(5))
print(nf2(7))

print "-"*10

# Creacion de un decorador

# Defenimos la funcion decoradora

def miDecorador(func):
    # Definimos la funcion que envuelve
    def decorador(a):
        print "Antes de llamar al decorado"
        print "He recibido a:",a
        #Llamamos al decorado
        func(a)
        #Regresamos de la ejecucion del decorado
        print "Ya regrese de la ejecucion del decorador"
    return decorador

# Decoramos la funcion
@miDecorador
def miFuncion(x):
    print "Estoy en mi funcion con x:",x

# Invocamos la funcion
miFuncion(5)
        
      
