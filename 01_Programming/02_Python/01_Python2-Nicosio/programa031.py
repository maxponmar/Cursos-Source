
# Excepciones
# El codigo que tiene riesgo se coloca en un bloque try
# en lugar de catch usamos except

# assert evalua una excepsion, si la evaluacion es falsa se levanta una
# excepcion de tipo AssertionError

def pares(n):
    assert(n%2==0)
    print "Es par"

pares(4)
pares(16)
#pares(5)

print "-"*10

try:
    print "vamos a intentar un impar"
    pares(5)
except AssertionError:
    print " fue un impar"
else:
    print "Era par"

print "-"*10

# Cuando deseamos capturar todas las excepciones
try:
    print "vamos a intentar un impar"
    pares(5)
except:
    print " fue un impar"
else:
    print "Era par"

# finally se usa para poner codigo que se ejecuta independientemente de  si la
# excepcion ocurre o no
try:
    print "vamos a intentar un impar"
    pares(5)
except:
    print " fue un impar"
else:
    print "Era par"
finally:
    print "Gracias por usar el programa"

print "-"*10

# argument da informacion sobre la excepcion
a="hola"

try:
    x=int(a)
    print x
except ValueError, Argument:
    print "El argumento dice ",Argument

# Se pueden tener multiples excepciones y levantar una excepcion usando raise

class Fue1(RuntimeError):
    def __init__(self):
        print "Desde la clase"

class Fue2(RuntimeError):
    def __init__(self, arg):
        self.args=arg

def checar(n):
    if n==1:
        raise Fue1
    if n==2:
        raise Fue2("Error")
    print "todo bien"

try:
    checar(2)
except Fue1:
    print "Excepcion para el 1"
except Fue2:
    print "Excepcion para el 2"

    
