"""
diccionario_1.py
script en python que implemente una agenda de contactos haciendo uso de un
diccionario. Para el diccionario las llaves serán los nombres de los contactos
y como valor estará una tupla que contenga el numero de telefono y el correo
electronico. se tendrá un menu con las siguientes opciones:

1) agregar un contacto
2) mostrar un contacto
3) buscar un contacto
4) modificar contacto
5) eliminar contacto
0) salir
"""

import os

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5

def mostrar_menu():
    os.system("cls")
    print(f"""                AGENDA
    {AGREGAR}) Agregar contacto
    {MOSTRAR}) Mostrar contacto
    {BUSCAR}) Buscar contacto
    {MODIFICAR}) Modificar contacto
    {ELIMINAR}) Eliminar contacto
    {SALIR}) Salir
    """)

def agregar_contactos(agenda):
    os.system("cls")
    print(f"                Agregar Contacto")
    nombre= input("Indique nombre: ")
    if agenda.get(nombre):
        print("Ya existe el contacto")
    else:
        telefono = input("ingrese telefono: ")
        mail = input("ingrese correo: ")
        agenda.setdefault(nombre, (telefono, mail) )
        print("Contacto agregado con exito!!")


def mostrar_contactos(agenda):
    os.system("cls")
    print(f"""              Mis Contactos""")
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f"Nombre: {contacto}")
            print(f"Telefono: {datos[0]}")
            print(f"Mail: {datos[1]}")
            print("$"*50)
    else:
        print("No hay contactos registrados!")


def buscar_contacto(agenda):
    os.system("cls")
    print(f"""              Buscar Contacto""")
    if len(agenda) > 0:
        nombre = input("ingrese el nombre a buscar: ")
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f"Nombre: {contacto}")
                print(f"Telefono: {datos[0]}")
                print(f"Mail: {datos[1]}")
                print("$"*50)
                encontrados += 1
        if encontrados == 0:
            print("no se encontró el contacto")
        else:
            print(f"se encontraron {encontrados} contactos!")
    else:
        print("No hay contactos registrados!")


def modificar_contactos(agenda):
    os.system("cls")
    print(f"""              Modificar Contacto""")
    if len(agenda) > 0:
        nombre = input("ingrese nombre: ")
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print("Información actual")
            print(f"Nombre: {nombre}")
            print(f"Telefono: {datos[0]}")
            print(f"Mail: {datos[1]}")
            print("$"*50)
            print("Ingresa los nuevos datos: ")
            telefono = input("Telefono: ")
            mail = input("Email: ")
            agenda[nombre] = (telefono, mail)
        else:
            print("no existe el contacto")
    else:
        print("No hay contactos registrados!")


def eliminar_contactos(agenda):
    os.system("cls")
    print(f"""              Eliminar Contacto""")
    if len(agenda) > 0:
        nombre = input("ingrese nombre: ")
        if agenda.get(nombre):
            agenda.pop(nombre)
            print("Contacto eliminado con exito!!")
        else:
            print("no existe el contacto")
    else:
        print("No hay contactos registrados!")


def main():
    continuar = True
    mi_agenda = {}
    while continuar:
        mostrar_menu()
        opc = int(input("ingrese una opción: "))
        if opc == AGREGAR:
            agregar_contactos(mi_agenda)
        elif opc == MOSTRAR:
            mostrar_contactos(mi_agenda)
        elif opc == BUSCAR:
            buscar_contacto(mi_agenda)
        elif opc == MODIFICAR:
            modificar_contactos(mi_agenda)
        elif opc == ELIMINAR:
            eliminar_contactos(mi_agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print("opción no valida")
        input("Presione enter para continuar")
    print("nos vemos!!")

if __name__ == "__main__":
    main()
