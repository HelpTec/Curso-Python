"""
repetitiva_desde_7.py
vamos a preguntar al usuario cantidad de numeros a regsitrar, le solicite
dichos valores y finalmente imprima el promedio de los mismos
"""
print("""                       calculadora de promedios            """)
acumulador = 0
total_datos = int(input("ingresa la cantidad de datos a promediar: "))

for valor in range(total_datos):
    dato = int(input("ingresa tu dato: "))
    acumulador = acumulador + dato
print(f"tu promedio es {acumulador/total_datos}")
print("fin del script")
