"""
repetitiva_mientras_3.py
script en python que le pida a un usuario ingresar su nombre y contraseña
y que de no validarlos lo siga pidiendo
"""

import os

USER = "Diego"
PASS = "El Negre"

user = " "
password = " "

while USER != user or PASS != password:
    os.system("cls")
    print("				kit-kot")
    user = input("usuario: ")
    password = input("contraseña: ")
    if USER != user or PASS != password:
        print("credenciales incorrectas, intenta denuevo")
        input("presiona enter para continuar")
else:
	print(f"bienvenido {USER}")
	input("presiona enter para continuar")
