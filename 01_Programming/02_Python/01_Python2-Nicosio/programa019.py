# Operaciones con sets

# Creacion de set con {}
"""
colores={"rojo","verde","azul"}
print type(colores)
print colores

# Copiar el set
masColores=colores.copy()
print masColores

# Remover todos los elementos de la lista
masColores.clear() # usa del para eliminar por completo el set
print masColores
"""
# Diferencia
a={1,2,3,4,5,6}
b={1,3,5}
"""
print a.difference(b)

x= a-b
print a,x

# difference_update
c={1,2,3,4,5,6}

c.difference_update(b)
print "c= ",c

# discard
b.discard(3)
print b

b.discard(9)

# remove, muestra error
d={1,2,3}
d.remove(2)
print d

# Marca error
#d.remove(9)
"""
# Interseccion
e = {1,3,5}
print a.intersection(e)

# isdisjoint regresa true si tienen una interseccion nula
f={10,11,120}

print a.isdisjoint(e)
print a.isdisjoint(f)

#issubset
s1={1,2,3,4,5,6,7,8,9,10}
s2={3,4,5}
s3={11,12,13,1}
print "---------"

print s2.issubset(s1)
print s1.issubset(s2)
print s3.issubset(s1)
print s1.issubset(s1)

# otra syntaxis
print "---------"
print s2<=(s1)
print s1<=(s2)
print s3<=(s1)
print s1<=(s1)


# superset
print "Superconjunto ---------------"

print s2>=(s1)
print s1>=(s2)
print s3>=(s1)

# proper subset. subconjunto propio. Es un superconjunto de A que no es igual a A

print "--------------"

print s2<s1
print s1<s2
print s1<s1

# proper superset, superconjunto propio. Es un superconjunto de A que no es igual a A

print "--------------"

s4={1,2,3,4,5,6,7,8,9,10,11,12}
print s4>s1
print s1>s4
print s1>s1


# pop, obtiene y remueve un elemento
print s4
print s4.pop()
print s4.pop()
print s4.pop()
print s4


