"""
procedimiento_6.py
script en python que implemente un procedimiento
en el que recibe el nombre y la edad del usuario
y en caso de que la edad sea mayor o igual que
18 le indique que ya es mayor de edad;
caso contrario le indique que es menor
"""

def mayoria_edad(nombre, edad):
	print(f"hola {nombre}, un gusto verte de nuevo")
	if edad >= 18:
		print("eres mayor de edad")
	else:
		print("aún eres menor")

mayoria_edad("Juan", 66)
