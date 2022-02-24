"""
selectiva_multiple_2.py
vamos a hacer un menu simple donde sea un listado con algunos paises
y si el usuario selecciona uno de ellos se le muestra la capital de dicho
pais
"""

ARGENTINA = 1
URUGUAY = 2
COLOMBIA = 3
MEXICO = 4
ECUADOR = 5
PERÚ = 6
print("""                    CAPITALES DE AMERICA
1) ARGENTINA
2) URUGUAY
3) COLOMBIA
4) MEXICO
5) ECUADOR
6) PERÚ
""")

opc = int(input("elige una opción: "))
if opc == ARGENTINA:
    print("BUENOS AIRES")
elif opc == URUGUAY:
    print("MONTEVIDEO")
elif opc == COLOMBIA:
    print("BOGOTÁ")
elif opc == ECUADOR:
    print("QUITO")
elif opc == MEXICO:
    print("CIUDAD DE MEXICO")
elif opc == PERÚ:
    print("LIMA")
else:
    print("no elegiste una opción valida")
print("fin del script")
