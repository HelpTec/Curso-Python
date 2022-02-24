"""
estructura_selectiva_doble_2.py
vamos a simular un sistema doble que chequee un usuario y contraseñas
el usuario deberá proporciónar nombre y contraseña. la app comprobara y validara
si coinciden los valores le dará la bienvenida, sino lo mandará a la mierda
"""
USER = "Diegue"
PASSWORD = "El negre"

print("proporciona los siguientes datos: ")
user = input("usuario: ")
password = input("contraseña: ")

if user == USER and password == PASSWORD:
	print("welcome... to the real world")
else:
	print("al lobby gordo teton")
print("fin del script")
