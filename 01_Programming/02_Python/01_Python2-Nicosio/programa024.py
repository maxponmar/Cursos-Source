# Expresiones regulares
# Se usan para filtrar textos y verificar si un texto concuerta con la expresion

# importamos el modulo re

import re

a=re.search("casa","La cada del casamentero")
print a

if re.search("casa","El estudiante es un casanova en la escuela"):
    print "1 Esta casa"
else:
    print "1 No esta casa"

if re.search("casa","El estudiante es un genio en la escuela"):
    print "2 Esta casa"
else:
    print "2 No esta casa"

if re.search(" casa ","El estudiante es un casanova en la escuela"):
    print "3 Esta casa"
else:
    print "3 No esta casa"


# Uso de . significa cualquier caracter
# cabal, academico

if re.search(" ca.","Saludos al mas academico"):
    print "Hay palabra que inicia con ca"
else:
    print "No hay palabra que inicia con ca"


# Uso de clases de caracteres, se usa [] para contener los caracteres
# Nico, Necio, Naco

if re.search("N[ie]c","Hola Nico"):
    print "Se encontro"
else:
    print "No se encontro"


# Un rango
# Nico, Neco, Noco, Nzco

if re.search("N[a-u]c","Hola Nico"):
    print "Se encontro"
else:
    print "No se encontro"


# Uso de complemento ^
if re.search("N[^ie]c","Hola Nico"):
    print "Se encontro"
else:
    print "No se encontro"

# Uso de match, para saber si una cadena inicia con una expresion
if re.match("N[ie]c","De Youtube Nicosiored es mi canal favorito"):
    print "Si inicia"
else:
    print "No inicia"

# Para saber si una cadena finaliza con una expresion

if re.search("N[ie]c$","De Youtube Nicosiored es mi canal favorito Nic"):
    print "Si finaliza"
else:
    print "No finaliza"

# Elemento opcional
# Nico, Nilo, Nio
if re.search("N[ie]c?o","Hola Nio"):
    print "Se encontro"
else:
    print "No se encontro"

# Cuantificador
# Busca que exista dos digitos

if re.search("[0-9]{2}","Hola 45 Nico"):
    print "Se encontro"
else:
    print "No se encontro"





