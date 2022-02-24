""""
listas_1.py
script en python que permita administrar operaciones sobre una lista.
dentro del programa existira una lista para almacenar el nombre de
diferentes frutas. para el control de la lista se mostrara un menu con
las opciones:
Agregar
Insertar
Mostrar lista
Buscar una fruta
Eliminar un registro
Ordenar una lista
Limpiar lista
Salir
"""

import os

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

frutas = []

def imprimir_menu():
    os.system("cls")
    print(f"""                          FRUTAS
    {AGREGAR}) AGREGAR
    {INSERTAR}) INSERTAR
    {MOSTRAR}) MOSTRAR
    {BUSCAR}) BUSCAR
    {ELIMINAR}) ELIMINAR
    {ORDENAR}) ORDENAR
    {LIMPIAR}) LIMPIAR
    {SALIR}) SALIR
    """)

def agregar_registro():
    print("             AGREGAR")
    nombre = input("Nombre: ")
    frutas.append(nombre)
    print("Registro agregado con exito")

def insertar_registro():
    print("             INSERTAR")
    nombre = input("Nombre: ")
    posicion = int(input("Posición: "))
    frutas.insert(posicion, nombre)
    print("Registro agregado con exito")

def mostrar_registros():
    print("             MOSTRAR REGISTROS")
    if len(frutas) > 0:
        for fruta in frutas:
            print(fruta)
    else:
        print("no hay registros aún")

def buscar_registros():
    print("             BUSCAR REGISTROS")
    if len(frutas) > 0:
        nombre = input("Nombre a buscar: ")
        if nombre in frutas:
            cantidad = frutas.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = frutas.index(nombre, inicio)
                print(f"{nombre} se encuentra en la posición {pos+1}")
                inicio = pos + 1
        else:
            print(f"{nombre} no ingresado en la lista")
    else:
        print("no hay registros aún")

def eliminar_registros():
    print("             ELIMINAR REGISTROS")
    if len(frutas) > 0:
        for i in range(len(frutas)):
            print(f"{i+1}. {frutas[i]}")
        print("0. Cancelar")
        pos = int(input(f"Posición a eliminar (1 - {len(frutas)}): "))
        if 0 < pos <= len(frutas):
            frutas.pop(pos-1)
            print("Registro eliminado con exito")
        else:
            print("acción cancelada")
    else:
        print("no hay registros que eliminar")

def ordenar_registros():
    print("             ORDENAR REGISTROS")
    if len(frutas) > 0:
        frutas.sort()
        print("Registros Ordenados alfabeticamente")
    else:
        print("no hay nada que ordenar")

def limpiar_registros():
    print("             LIMPIAR REGISTROS")
    frutas.clear()
    print("Registros borrados con exito")

def Main():
    continuar = True
    while continuar:
        imprimir_menu()
        opc = int(input("Selecciona una opción: "))
        os.system("cls")
        if opc == AGREGAR:
            agregar_registro()
        elif opc == INSERTAR:
            insertar_registro()
        elif opc == MOSTRAR:
            mostrar_registros()
        elif opc == BUSCAR:
            buscar_registros()
        elif opc == ELIMINAR:
            eliminar_registros()
        elif opc == ORDENAR:
            ordenar_registros()
        elif opc == LIMPIAR:
            limpiar_registros()
        elif opc == SALIR:
            print("Adios")
            continuar = False
        else:
            print("opción no valida")
        input("presione enter para continuar")

if __name__ == "__main__":
        Main()
