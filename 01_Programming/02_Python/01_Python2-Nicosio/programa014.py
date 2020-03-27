# Comparacion entre listas

lista1 =[100,"Hola"]
lista2=[30,"Bye"]

print cmp(lista1,lista1)

# Obtencion del maximo
lista3 = [50,70,23,57,90,10,45,23,11,23,65]
print "Maximo ",max(lista3)

# Obtencion del minimo
print "Minimo ",min(lista3)

# Adicion de elemento

print lista3
lista3.append(14)
print lista3

# Conteo de un elemento en la lista

print lista3.count(23)

# Obtenemos el indice mas bajo del elemento repetido

print lista3.index(23)

# Otra forma de unir listas
lista1.extend(lista2)
print lista1

# Insertar en un indice en particular
print lista1
lista1.insert(2,77)
print lista1

print "-------------"
# Hacer pop del ultimo objeto de la lista
print lista1
print lista1.pop()
print lista1

# Hacer pop de un objeto en un indice en particular
print lista1
print lista1.pop(2)
print lista1

# Hace reversa de la lista
lista1.reverse()
print lista1

# Ordena la lista
lista3.sort()
print lista3
