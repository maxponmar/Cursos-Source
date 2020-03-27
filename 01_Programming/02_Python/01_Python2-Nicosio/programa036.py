# Metodo estatico
# Metodo de clase
# Funciones de interfaz
# Propiedades

class Persona:
    "Esta es la clase para personas"
    
    # Atributo public0
    valor=0

    # Atributo privado
    __dato=20

    # inicializamos
    def __init__(self,nombre,edad):
        print "Estamos en __init__"
        self.Nombre=nombre
        self.Edad=edad

    # Definimos un metodo
    def muestra(self):
        print "Mi nombre es ", self.Nombre
        print "Mi edad es ", self.Edad
        print "El valor guardado es", self.valor
        print "El dato es ", self.__dato
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

    # Creamos un metodo estatico
    @staticmethod
    def mensaje(msg):
        print "Tienes este mensaje: ",msg

    # Creamos un metodo de clase
    # Se usan en el patron farica
    @classmethod
    def autor(cls):
        print "La clase ", cls.__name__
        print "Fue creada por Nicosio"

    # Creamos funciones de interfaz para __dato

    def get_dato(self):
        return self.__dato

    def set_dato(self,pDato):
        print "En propiedad"
        self.__dato=pDato

    # Creamos propiedades para Nombre
    @property
    def Nombre(self):
        return self.Nombre

    @Nombre.setter
    def Nombre(self, pDato):
        self.Nombre = pDato

# Hacemos uso de funciones de interfaz
persona1=Persona("Susana",20)
persona1.muestra()
persona1.set_dato(67)
persona1.muestra()

# Hacemos uso de propiedades
p=persona1

p.Nombre="Victor"
print p.Nombre
print persona1.Nombre
p.muestra()
persona1.muestra()
print "-"*30
print "-"*30
# Uso de los metodos
Persona.mensaje("Saludos a todos")
Persona.autor()

    
    

    
