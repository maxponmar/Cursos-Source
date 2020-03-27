
# Lectura de archivos

# r - solo lectura
# rb - solo lectura en formato binario
# r+ - lectura y escritura, apuntador al inicio del archivo
# rb+ - igual que el anterior pero en binario
# w - solo escritura
# wb - solo escritura en binario
# w+ - escritura y lectura, sobre escribe el archivo si existe
# wb+ - igual que el anterior pero en binario
# a  abre para append (adicion), el apuntar al final del archivo
# ab - igual pero en binario
# a+ abre para append o lectura, el apuntador al final del archivo
# ab+ - igual pero en binario


# Arbrimos el archivo para lectura
archivo = open("mitexto.txt","r")

# Recorremos el archivo linea por linea
for linea in archivo:
    print linea.rstrip()

print "Nombre: ", archivo.name
print "Cerrado?: ", archivo.closed
print "Modo de apertura : ", archivo.mode

# Cerramos el archivo
archivo.close()

print "-"*20


# Abrimos el archivo para escritura
archivo=open("otrotexto.txt","a")
n=0

# Escribimos 5 letras
while n<5:
    texto=raw_input("Dame un texto ")
    archivo.write(texto+"\n")
    n=n+1
# Cerramos el archivo
archivo.close()


# Abrir el archivo a una lista
lista = open("mitexto.txt","r").readlines()
print lista
print"-"*20

archivo=open("mitexto.txt","r")

# Vemos la posicion
pos=archivo.tell()
print "Posicion ", pos

# Colocamos en una posicion
# 0 - incio
# 1 - posicion actual
# 2 - final del archivo

archivo.seek(5,0)
cadena=archivo.read(8)
print cadena
pos=archivo.tell()
print "Posicion ",pos

archivo.close()

# Serializacion
# Tres protocolos, 0-ascii, 1-compacto, 2-clases optimizadas

# Importamos el modulo
import pickle

# Creamos al objeto a serializar
lista1=[5,"hola"]
lista2=[7.8,"Python",True]

# Abrimos para escritura
archivo=open("misdatos.dato","w")

#Serializamos
pickle.dump(lista1,archivo)
pickle.dump(lista2,archivo)

# Cerramos
archivo.close()

# Deserializamos
archivo=open("misdatos.dato","r")
lst1=pickle.load(archivo)
lst2=pickle.load(archivo)

print lst1
print lst2

archivo.close()
