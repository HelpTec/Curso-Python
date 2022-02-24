"""
funciones_6.py
script en python que implmenete una función encargada de convertir una
cantidad de segundos a minutos y segundos. la función deberá recibir
como argumento una cantidad de segundos y deberá regresar la cantidad
de minutos y segundos equivalente.
"""

def segundos_a_minutos(segundos):
    m = segundos // 60
    s = segundos % 60
    return m, s

print("conversor de segundos a minutos y segundos")
segundos = int(input("indique segundos: "))

min, seg = segundos_a_minutos(segundos)

print(f"el resultado es {min}:{seg}")
