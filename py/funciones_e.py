"""
funciones_e.py
script en python que implmenete un programa para realizar las siguientes
conversiones:
- segundos a minutos: recibe segundos y devuelve minutos y segundos
- segundos a horas: recibe segundos y regresa horas, minutos y segundos
- minutos a segundos: recibe minutos y segundos y regresa segundos
- minutos a horas: recibe minutos y segundos y regresa horas minutos y
segundos
ademas deberá implmenetarse un metodo para imprimir el menú de opciones
y la ejecución del programa debe comenzar desde el procedimiento "main".
el programa debe seguir en ejecución mientras el usuario no decida salir.
"""
import os

def segundos_a_minutos(segundos):
    m = segundos // 60
    s = segundos % 60
    return m, s

def segundos_a_horas(segundos):
    h = segundos // 3600
    m = segundos // 60
    s = segundos % 60
    return h, m, s

def minutos_a_segundos(segundos, minutos):
    s = minutos * 60 + segundos
    return s

def minutos_a_horas(segundos, minutos):
    h = minutos // 60
    m = segundos // 60
    s = segundos % 60
    return h, m, s

SEGUNDOS_A_MINUTOS = 1
SEGUNDOS_A_HORAS = 2
MINUTOS_A_SEGUNDOS = 3
MINUTOS_A_HORAS = 4
SALIR = 5

def menu():
    print(f'''                      Conversiones
{SEGUNDOS_A_MINUTOS}) Segundos a minutos
{SEGUNDOS_A_HORAS}) Segundos a horas
{MINUTOS_A_SEGUNDOS}) Minutos a segundos
{MINUTOS_A_HORAS}) Minutos a horas
{SALIR}) Salir''')

def main():
    continuar = True
    while continuar:
        os.system("cls")
        menu()
        opc = int(input("seleccione una opción: "))
        if opc == 1:
            segundos = int(input("indique cantidad de segundos: "))
            min, seg = segundos_a_minutos(segundos)
            print(f"el resultado es {min}:{seg}")
            input("presione enter para continuar")
        elif opc == 2:
            segundos = int(input("indique cantidad de segundos: "))
            hor, min, seg = segundos_a_horas(segundos)
            print(f"el resultado es {hor}:{min}:{seg}")
            input("presione enter para continuar")
        elif opc == 3:
            segundos = int(input("indique cantidad de segundos: "))
            minutos = int(input("indique cantidad de minutos: "))
            seg = minutos_a_segundos(segundos, minutos)
            print(f"el resultado es {seg}")
            input("presione enter para continuar")
        elif opc == 4:
            segundos = int(input("indique cantidad de segundos: "))
            minutos = int(input("indique cantidad de minutos: "))
            hor, min, seg = minutos_a_horas(segundos, minutos)
            print(f"el resultado es {hor}:{min}:{seg}")
            input("presione enter para continuar")
        elif opc == 5:
            continuar = False
    else:
        print("adios")

if __name__ == "__main__":
    main()
