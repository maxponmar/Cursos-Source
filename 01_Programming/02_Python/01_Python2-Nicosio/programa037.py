# Uso de Slots y atributos dinamicos
# Nuestra clase debe de descender de object

class Persona(object):
    "Esta es la clase para personas"

    # Usar __slots__ para evitar los atributos dinamicos
    __slots__=('Nombre','Edad')

    # No hay constructor explocito, pero usamos __init__
    def __init__(self,nombre,edad):
        self.Nombre=nombre
        self.Edad=edad

    # Definimos un metodo
    def muestra(self):
        print "Mi nombre es ", self.Nombre
        print "Mi edad es ", self.Edad
        print "-"*20

     # No hay destructor explicito, pero usamos __del__
    def __del__(self):
        print "Bye desde: ", self.Nombre

Persona1=Persona("Aldo",18)
Persona1.muestra()

# Creamos un atributo dinamico

Persona1.peso=60
print Persona1.peso
