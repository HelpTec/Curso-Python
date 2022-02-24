
"""
selectiva_doble_1.py
script simple que solicite al usuario adivinar un numero entre 1 y 109
si el usuario adivina entonces felicita por su logro y en caso contrario
le indica cual era el numero
"""

import random
valor = random.randint(1, 10)
print("acabo de generar un numero secreto entre 1 y 10")
usuario = int(input("cual crees que sea mi numero secreto? "))
if usuario == valor:
	print("felicidades!")
else:
	print(f"{valor}")
