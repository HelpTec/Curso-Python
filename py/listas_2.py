
"""
listas_2.py
script en python que calcula y muestra la suma de dos matrices
cuadradas (misma cantidad de renglones y columnas) generadas
aleatoriamente. Utilizar comprensión de listas para generar las
matrices de forma aleatoria
"""

import random

N = 3

print(f"Programa que calcula la suma de matrices de tamaño {N}x{N}")

m1 = [[random.randint(1, 50) for j in range(N)]for i in range(N)]
m2 = [[random.randint(1, 50) for j in range(N)]for i in range(N)]
resultado = [[0]*N for i in range(N)]
"""
for renglon in range(N):
    for columna in range(N):
        resultado[renglon][columna]=m1[renglon][columna]+m2[renglon][columna]
"""
resultado = [ [m1[i][j]+m2[i][j] for j in range(N)]for i in range(N) ]

"""
for i in range(N):
    if i == N//2:
        print(f"{m1[i]} + {m2[i]}  =  {resultado[i]}")
    else:
        print(f"{m1[i]}   {m2[i]}   {resultado[i]}")
"""

for i in range(N):
    print(f"{m1[i]} + {m2[i]}  =  {resultado[i]}") if i == N//2 else print(f"{m1[i]}   {m2[i]}   {resultado[i]}")
