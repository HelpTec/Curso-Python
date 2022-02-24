
"""
repetitiva_desde_2.py
script en python que imprima los numeros pares desde el 2 hasta el 20 haciendo
uso de un ciclo for
"""
#hay varias formas de hacer esto

print("programa que muestra los numeros pares desde el 2 hasta el 20")

print("metodo 1")

for numero in range(1, 11):
	print(f"par: {numero*2}")

print("nos vemos")

print("metodo 2")

for numero in range (1, 21):
	if numero % 2 == 0:
		print(f"par: {numero}")
print("nos vemos")

print("*"*20)

print("tercer metodo")

for par in range(2, 21, 2):
	print(f"par:{par}")
print("nos vemos")
