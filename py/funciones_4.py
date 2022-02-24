"""
funciones_4.py
script en python que implmenete funcion para
calcular el area de un triangulo. dicha funcion
debera recibir como argumento el valor de la base y altura y regresara el area calculada
"""
def area_triangulo(altura, base):
    return base * altura / 2
altura = float(input("ingrese altura: "))
base = float(input("ingrese base: "))


print(f"{area_triangulo(altura, base)}")
