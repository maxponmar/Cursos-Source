import re

# findall regresa una lista con todos los matches

encontrados=re.findall("c[ao]s","El casanova no se casa ni va al casamiento, por que la cosa es complicada")
print encontrados

# alteraciones
b= "Yo se programar en python"
mo= re.search("(c|java|python)",b)
if mo:
    print "Sabes programar"
else:
    print "Aprende otro lenguaje"

# Split
mensaje="Este es un test de separacion, division"
partes= re.split(" ", mensaje)
print partes

# Remplazar
mensaje2="Yo hablo ingles y no soy ingles"
sustituido=re.sub("ingles","espanol",mensaje2)
print sustituido


# Metodos utiles para cadenas

mensaje = "hola A todos"
print mensaje.capitalize()

palabra="Python"
print palabra.center(15,"-")

mensaje = "Hola a todos los que ven la ola en Holanda"
print mensaje.count("ola")

texto="345!"
print texto.isalnum()
print texto.isalpha()
print texto.isdigit()
