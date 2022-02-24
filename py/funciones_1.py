"""
funciones_1.py
script en python que implmenete función para calcular area
de un triangulo
"""
def area_triangulo():
    base = float(input("ingresa la base: "))
    altura = float(input("ingresa la altura: "))
    area = base * altura / 2
    return area

a = area_triangulo()

print(f"{a}")
