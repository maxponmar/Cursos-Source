# Metaclases

# Una clase es un objeto, es en realidad una instancia de una metaclase
# La metaclase de default es type
# Intancia --Intanceof--> clase --InstanceOf--> metaclasee

# Hacen uso de metodos magicos. Operadores y comportamientos a los que se les
# puede hacer override

opcion1=input("Desdea colocar el duplicador en valores 1? 1.si 2.no")
opcion2=input("Desdea colocar el duplicador en valores 2? 1.si 2.no")

def duplicador(self):
    self.a=self.a*2
    self.b=self.b*2
    print "Estoy en duplicador"

class valores1:
    pass

    def __init__(self,pa,pb):
        self.a=pa
        self.b=pb

    def muestra(self):
        print "El valor de a ", self.a
        print "El valor de b ",self.b

# Adicionamos el metodo dinamicamente a la clase
if opcion1==1:
    valores1.duplicador=duplicador

class valores2:
    pass

    def __init__(self,pa,pb):
        self.a=pa
        self.b=pb

    def muestra(self):
        print "El valor de a ", self.a
        print "El valor de b ",self.b

# Adicionamos el metodo dinamicamente a la clase
if opcion2==1:
    valores2.duplicador=duplicador


# Instanciamos
val1=valores1(5,3)
val2=valores2(10,22)

# Usamos las instancias
print "Valores 1"
val1.muestra()
#val1.duplicador()
if opcion1==1:
    val1.duplicador()
    val1.muestra()
print "-"*20

print "Valores 2"
val2.muestra()
if opcion2==1:
    val2.duplicador()
    val2.muestra()
print "-"*20
