# Iterador - nos permite recorrer una estructura de datos sin que nos
# interese conocer la forma como trabaja esa estrctura, usamos for

# Generador - es una funcion especial que nos permite implementar iteradores

# internamente el for trabaja con un iterador que va pididendo el elemento
# siguiente hasta que recibe StopIteration

dias =["lunes","martes","miercoles","jueves","viernes"]
for d in dias:
    print d

print "-"*10

dias =["lunes","martes","miercoles","jueves","viernes"]

# Se invoca iter en la estructura y nos regresa un iterable
mi_iterador=iter(dias)

# Usamos el iterable con next para obtener el elemento siguiente
print next(mi_iterador)
print next(mi_iterador)
print next(mi_iterador)
print next(mi_iterador)

# Cuando recibicos StopIteration, sabemos que ya no hay mas elemntos
print next(mi_iterador)
#print next(mi_iterador)

print "-"*10

dias =["lunes","martes","miercoles","jueves","viernes"]

# Aqui ya estamos mas cerca de construir un iterador para las listas

# Se invoca iter en la estructura y nos regresa un iterable
mi_iterador=iter(dias)

# Creamos un ciclo pero tenemos que tener una excepcion para cachar cuando
# ya no hay mas elementos
while mi_iterador:
    try:
        d=next(mi_iterador)
        print d
    except StopIteration:
        print "no hay mas elementos, forzamos la salida"
        break
print "-"*10

# Un generador es una funcion que regresa un objeto generator
# Un gerator se puede ver como una funcion que produce una secuencia de
# resultados en lugar de un solo objeto. Estos son producidos al iterar
# yield es lo que convierte a una funcion en un iterador
# Se termina la ejecucion cuando se ha llegado a yield y el valor es regresado
# Cuando se usa next, se acanza al siguiente yield
# Cualquier estado intermedio de las variables se guarda entre invocaciones
# cosa que no sucede en las funciones

def dias_generador():
    yield("lunes")
    yield("martes")
    yield("miercoles")
    yield("jueves")
    yield("viernes")

dias=dias_generador()
print next(dias)
print next(dias)
print next(dias)
print next(dias)
print next(dias)
#print next(dias)
print "-"*20

# Creamos un generador para potencias de dos

def potencias2():
    b=1
    while b>0:
        yield b
        b=b+b

binarios=potencias2()

for x in binarios:
    print x
    if x>100:
        break
print "-"*10

# Creamos un generador para potencias de 2 hasta cierto numero
def potencias2():
    b=1
    while b>0:
        yield b
        b=b+b
        if b>300:
            raise StopIteration
        

binarios=potencias2()

for x in binarios:
    print x
