"""
repetitiva_desde_e.py
ejercisio de script que muestre un cronometro en formato de 24 con horas
minutos y segundos. ese cronometro deberá empezar en 00:00:00 y deberá terminar
en 23:59:59
"""
import os
import time
for hora in range(0, 23, 1):
    for minutos in range(0, 59, 1):
        for segundos in range(0, 59, 1):
            os.system("cls")
            print(f"{hora}:{minutos}:{segundos}")
            time.sleep(1)
print("fin del script")
