"""
procedimientos_3.py
script en python que dentro de un procedimiento solicite nombre y edad del
usuario devolviendole si es mayor de edad o no.
"""
def mayoria_edad():
    nombre = input("como te llamas?: ")
    edad = int(input("que edad tienes?: "))
    if edad >= 18:
        print("ya eres mayor de edad")
    else:
        print("aún eres menor")

mayoria_edad()

print("nos vemos")
