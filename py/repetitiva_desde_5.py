"""
repetitiva_desde_5.py
script en python que muestre las tablas del 1 al 10
cada tabla mostrada hasta su 10 multiplo
"""
import os
for numero in range (1, 11):
    os.system("cls")
    print(f"            	tabla del {numero}")
    for multiplo in range (1, 11):
	       print(f"{numero} x {multiplo} = {numero * multiplo}")
    input("presiona enter para continuar")

print("nos vemos")
