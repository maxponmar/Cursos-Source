class Persona:
    "Esta es la clase para personas"

    # Variable de clase
    cantidad=0;
    
    # Atributo public
    valor=0

    # Atributo privado
    __dato=20

    # usamos __init__ para inicializar
    def __init__(self,nombre,edad):
        #print "Estamos en __init__"
        self.Nombre=nombre
        self.Edad=edad

    # Definimos un metodo

    def muestra(self):
        print "Mi nombre es ", self.Nombre
        print "Mi edad es ", self.Edad
        print "El valor guardado es", self.valor
        print "El dato es ", self.__dato
        print "La cantidad es ",Persona.cantidad
        print "-"*20

    # Otro metodo
    def muestraSaludo(self):
        print "Hola, soy ",self.Nombre

    # Metodo para la variable de clase
    def ponCantidad(self,cant):
        Persona.cantidad=cant
        
    # No hay destructor explicito, pero usamos __del__

    def __del__(self):
        print "Bye desde: ", self.Nombre

# Hacemos una herencia
class Empleado(Persona):

    # Atributo de empleado
    sueldo=0

    # Inicializacion
    def __init__(self,nombre,edad, salario):
        Persona.__init__(self,nombre, edad)
        self.sueldo=salario

    # Metodo que aprovecha el metodo de la clase padre
    def muestraEmpleado(self):
        Persona.muestra(self)
        print "El sueldo es ",self.sueldo

    # Override a un metodo
    def muestraSaludo(self):
        print "Hola, tengo trabajo y soy ",self.Nombre

# Probamos la variable de clase
persona1=Persona("Aldo",18)
persona2=Persona("Ana",20)

persona1.valor=50

persona1.muestra()
persona2.muestra()

print "Ponemos cantidad"
persona1.ponCantidad(100)
print "-"*20

persona1.muestra()
persona2.muestra()
print "-"*20
# Probamos la clase con herencia
empleado1=Empleado("Juan",25,50000)
empleado1.muestraEmpleado()
empleado1.muestraSaludo()


    
