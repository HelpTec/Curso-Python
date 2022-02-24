"""
selectiva_multiple_e.py
script en Python que simula una calculadora con las operaciones aritméticas básicas. El menú mostrado será el siguiente:

1) Suma
2) Resta
3) Multiplicación
4) División
5) División Entera
6) Módulo
7) Potencia

Nota: Primero solicita la opción correspondiente a la operación a realizar y posteriormente solicita los dos operandos como datos enteros.
"""
SUMA = 1
RESTA = 2
MULTIPLICACIÓN = 3
DIVISIÓN = 4
DIVISIÓNENTERA = 5
MODULO = 6
POTENCIA = 7
print("""
1) Suma
2) Resta
3) Multiplicación
4) División
5) División Entera
6) Módulo
7) Potencia
""")
opc = int(input("elija una opción: "))
op1 = int(input("indique primer operando: "))
op2 = int(input("indique segundo operando: "))
if opc == SUMA:
    res = op1 + op2
    print(f"su cuenta dá {res}")
elif opc == RESTA:
    res = op1 - op2
    print(f"su cuenta dá {res}")
elif opc == MULTIPLICACIÓN:
    res = op1 * op2
    print(f"su cuenta dá {res}")
elif opc == DIVISIÓN and op1 == 0 or op2 == 0:
    print("no se puede dividir por 0")
elif opc == DIVISIÓN:
    res = op1 / op2
    print(f"su cuenta dá {res}")
elif opc == DIVISIÓNENTERA:
    res = op1 // op2
    print(f"su cuenta dá {res}")
elif opc == MODULO:
    res = op1 % op2
    print(f"su cuenta dá {res}")
elif opc == POTENCIA:
    res = op1 ** op2
    print(f"su cuenta dá {res}")
else:
    print("su operación no pudo hacerse")
print("fin del script")
