# Definimos la clase

class Persona:
    "Esta es la clase para personas"

    # Atributo public
    valor=0

    # Atributo privado
    __dato=20

    # No hay constructor explicito, pero usamos __init__
    def __init__(self,nombre,edad):
        print "Estamos en __init__"
        self.Nombre=nombre
        self.Edad=edad

    # Definimos un metodos

    def muestra(self):
        print "Mi nombre es ", self.Nombre
        print "Mi edad es ", self.Edad
        print "El valor guardado es"; self.valor
        print "El dato es ", self.__dato
        print "-"*20

    # No hay destructor explicito, pero usamos __del__

    def __del__(self):
        print "Bye desde: ", self.Nombre


# Imprimimos el doc string
print Persona.__doc__

# Creamos la instancia
persona1= Persona("Aldo",18)

# Accedemos a atributo
persona1.valor=5
# Invocamos metodo
persona1.muestra()

# Un atributo privado
persona1.__dato=3
print "Intento imprimir el dato ", persona1.__dato
print "-"*20
# Invocamos metodo
persona1.muestra()


# Creamos otra instancia
persona2=Persona("Ana",20)
print "-"*20

# Eliminamos la otra instancia
del persona1
print "-"*20
persona2.muestra()
