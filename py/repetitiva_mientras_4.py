"""
repetitiva_mientras_4.py
scrypt en python que muestre un menu con nombres de personajes de un juego y
al elegir una opción hable de algunas caracteristicas de ellos
"""
import os

MALZAHAR = 1
ZED = 2
GALIO = 3
SETT = 4
VEIGAR = 5
LUCIAN = 6
SALIR = 7
continuar = True

while continuar:
    os.system("cls")
    print(f"""======================================================================
                            BIENVENIDOS A UN LOLCTIONARY
===============================================================================
LISTA DE CAMPEONES:
{MALZAHAR}) MALZAHAR
{ZED}) ZED
{GALIO}) GALIO
{SETT}) SETT
{VEIGAR}) VEIGAR
{LUCIAN}) LUCIAN
{SALIR}) SALIR
===============================================================================
""")
    opc = int(input("elige una opción o escribe salir para cerrar el programa: "))
    if opc == MALZAHAR:
        print("mago de mid lane enfocado en control y objetivos")
        input("presiona enter para elegir otra opción")
    elif opc == ZED:
        print("asesino de midlane enfocado en conseguir kills")
        input("presiona enter para elegir otra opción")
    elif opc == GALIO:
        print("tanque de midlane enfocado en proteger el equipo y su definitiva")
        input("presiona enter para elegir otra opción")
    elif opc == SETT:
        print("pick exotico mezcla de luchador con asesino en midlane")
        input("presiona enter para elegir otra opción")
    elif opc == VEIGAR:
        print( "mago enfocado en daño con potencial de carry")
        input("presiona enter para elegir otra opción")
    elif opc == LUCIAN:
        print("tirador en mid, cosa de trolos")
        input("presiona enter para elegir otra opción")
    elif opc == SALIR:
            continuar = False
    else:
        input("opción no valida, presiona enter para continuar")
else:
    print("nos vemos!")
