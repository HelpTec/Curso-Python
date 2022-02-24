"""
estructura_repetitiva_desde_4.py
script de python que muestre la tablaa de multiplicar de un numero ingresado
por el usuario. el usuario tambien podra ingresar hasta que valor llegará la
tabla de multiplicar
"""
numero = int(input("¿de que numero deseas ver la tabla de multiplicar? "))
limite = int(input("hasta que multiplo deseas ver? "))
print(f"	           tabla del {numero}")
for multiplo in range (limite + 1):
	print(f"{numero} x {multiplo} = {numero * multiplo}")

print("nos vemos")
