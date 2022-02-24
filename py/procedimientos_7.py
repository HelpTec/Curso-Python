"""
procedimientos_7.py
script en python que implemente un procedimiento dentro del cual se
muestre la tabla de multiplicar de un numero recibido como argumento.
el procedimiento contará con un segundo argumento que
indicará hasta que multiplo se mostrará la
tabla de multiplicar. ese segundo argumento
tendrá como valor por omisión el numero 10
"""

def tabla_multiplicar(numero, limite=10):
    print(f"""		tabla de multiplicar del {numero}""")
    for i in range(1, limite+1):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(7)
tabla_multiplicar(5, 13)

print("nos vemos")
