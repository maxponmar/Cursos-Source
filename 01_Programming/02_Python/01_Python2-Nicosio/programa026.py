# Operador lambda
# Crea funciones anonimas que se usan en el momento que hacen falta
# Generalmente se usan con filter(), map(), reduce()
# lambda arg1, ar2,...: expresion

valor = lambda a,b:a*a+2*a*b+b*b
print valor(2,3)

# Uso de map
# invoca una funcion haciendo uso de una secuencia
print "-"*20
def cuadrados(valor):
    return valor*valor

valores=[2,5,10]

resultados=map(cuadrados,valores)

print resultados
print "---- map con lambda ----"
# Uso de map con lambda

valores=[2,5,10]

resultados=map(lambda x: x*x, valores)
print resultados

# Uso de filter
# Filtra los elementos de una secuencia dependiendo del true o false
# regresado por una funcion
print "--- filter ---"

def impares(valor):
    return (valor%2)!=0

valores =[1,4,5,7,8,9,10,12,15,17,18,2]

filtrados=filter(impares,valores)
print filtrados

# Filtar con lambda
print "--- filter con lambda ---"
filtrados=filter(lambda x: x%2!=0, valores)
print filtrados

# Uso de reduce
# Aplica una funcion de manera continua a una secuencia de valores
# Y regresa un unico valor
# [a1,a2,a3,a4,a5]
# b1=fun(a1,a2)
# b2=fun(b1,a3)
# b3=fun(b2,a4)
# b4=fun(b3,a5) -> resultado final

valores=[1,2,3,4,5]
print "-- reduce --"
def suma(a,b):
    return a+b

r=reduce(suma,valores)
print r

# Con lambda
print "--reduce con lambda---"
r=reduce(lambda a,b:a+b, valores)
print r
