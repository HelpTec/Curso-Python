"""
funciones_3.py
script en python que nos permita pasar de grados farenheit a celsius
con una funcion encargada de la conversión
"""
def farenheit_a_celsius():
    f = float(input("grados farenheit: "))
    c = (f-32) / 1.8
    return c

celsius = farenheit_a_celsius()

print("programa que convierte grados farenheit a celsius")
print(f"en celsius sería: {celsius: .2f}")
print("nos vemos")
