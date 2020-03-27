# Uso de in, verifica si un objeto existe adentro de un objeto contenedor iterable
"""
nombre = input("Dame tu nombre ")

if nombre in["Nicosio", "Juan","Susana","Vegeta"]:
    print "Conozco ese nombre"
else:
    print "No conozco ese nombre"

# Uso de is, compara las instancias no los valores
"""
a=[2,3,5]
b=[2,3,5]
c=a

if a==b:
    print "a y b tienen el mismo valor"

if a is b:
    print "a y b son la misma instancia"
else:
    print "a y b no son la misma instancia"

if c is a:
    print "a y c son la misma instancia"
else:
    print "a y c no son la misma instancia"
