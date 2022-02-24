"""
archivos_7.py
script en python que implementa una agenda de contactos haciendo uso de un
diccionario. para el directorio las llaves serán los nombres de los contactos
y como valor estará una tupla que contenga numero telefonico y el correo
electronico. la agenda se guardará en un archivo de texto del cual se podrán
recuperar contactos y en el cual se podrán agregar los nuevos contactos
registrados. se tendrá un menu con las siguientes opciones:

1) Agregar contacto
2) Mostrar contactos
3) Buscar contacto
0) Salir
"""

import pathlib
import os

AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
SALIR = 0

def menu():
    print(F"""                  AGENDA DE CONTACTOS CON ARCHIVO

    OPCIONES
    {AGREGAR}) AGREGAR CONTACTO
    {MOSTRAR}) MOSTRAR CONTACTOS
    {BUSCAR}) BUSCAR CONTACTO
    {SALIR}) SALIR""")

def cargar_archivo(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(",")
                agenda.setdefault(contacto, (telefono, email))
    else:
        with open(nombre_archivo, "w") as archivo:
            pass

def agregar_contacto(agenda, nombre_archivo):
    os.system("cls")
    print("AGREGAR CONTACTO")
    nombre = input("Ingrese nombre de contacto: ")
    if agenda.get(nombre):
        print("Ya existe el contacto")
    else:
        telefono = input("ingrese telefono: ")
        mail = input("ingrese correo: ")
        agenda.setdefault(nombre, (telefono, mail) )
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"{nombre}, {telefono}, {mail}\n")
        print("Contacto agregado con exito!!")

def mostrar_contactos(agenda):
    os.system("cls")
    print(f"""              MIS CONTACTOS""")
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f"Nombre: {contacto}")
            print(f"Telefono: {datos[0]}")
            print(f"Mail: {datos[1]}")
            print("*"*50)
    else:
        print("No hay contactos registrados!")

def buscar_contacto(agenda):
    os.system("cls")
    print(f"""              BUSCAR CONTACTO""")
    if len(agenda) > 0:
        nombre = input("ingrese el nombre a buscar: ")
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f"Nombre: {contacto}")
                print(f"Telefono: {datos[0]}")
                print(f"Mail: {datos[1]}")
                encontrados += 1
                print("*"*50)
        if encontrados == 0:
            print("no se encontró el contacto")
        else:
            print(f"se encontraron {encontrados} contactos!")
    else:
        print("No hay contactos registrados!")


def main():
    continuar = True
    agenda = {}
    nombre_archivo = "agenda.txt"
    cargar_archivo(agenda, nombre_archivo)
    while continuar:
        os.system("cls")
        menu()
        opc = int(input("Ingrese la opción deseada: "))
        if opc == 1:
            agregar_contacto(agenda, nombre_archivo)
        elif opc == 2:
            mostrar_contactos(agenda)
        elif opc == 3:
            buscar_contacto(agenda)
        elif opc == 0:
            continuar = False
        else:
            print("Opción no valida")
        input("Presione enter para continuar")
    print("Nos vemos!")

if __name__ == "__main__":
    main()
