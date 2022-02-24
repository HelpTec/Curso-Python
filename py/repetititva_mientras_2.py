"""
repetitiva_mientras_2.py
script en python que sume numeros pares y multiplique numeros impares
mientras el usuario no ingrese un 0. se debera utilizar la estructura repetitiva
"mientras" para solicitar al usuario un numero y dependiendo del numero lo suma
o lo multiplica
"""

print("""hola, ingresá un numero, si es par lo voy a sumar, si es impar lo voy
a multiplicar. poné 0 para salír""")

suma = 0
multiplicación = 1
numero = -1

while numero != 0:
    numero = int(input("ingresa un numero: "))
    if numero == 0:
        print("adios")
    elif numero % 2 == 0:
        suma = numero + suma
        print(f"{suma}")
    else:
        multiplicación = numero * multiplicación
        print(f"{multiplicación}")
