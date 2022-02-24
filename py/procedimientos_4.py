"""
procedimientos_4.py
script en python que muestre un menú ciclico; dicho menu será
implementado en un procedimiento
"""

import os

ESP = 1
ING = 2
NO_SUBS = 3
SALIR = 4

def mostrar_menu():
	print(f"""		SUBTÍTULOS
	{ESP}) ESPAÑOL
	{ING}) INGLÉS
	{NO_SUBS}) SIN SUBTITULOS
	{SALIR}) SALIR
	""")

continuar = True
while continuar:
    os.system("cls")
    mostrar_menu()
    opc = int(input("selecciona una opción: "))
    os.system("cls")
    if opc == ESP:
        print("subtitulos en español")
    elif opc == ING:
        print("subtitulos en ingles")
    elif opc == NO_SUBS:
        print("subtitulos apagados")
    elif opc == SALIR:
        continuar = False
        print("nos vemos")
    else:
        print("opción no valida")
    input("presiona enter para continuar")
