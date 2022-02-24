"""
selectiva_simple_e.py
ejercisio indicado por el maestro. se redondean calificaciones
"""

calificación = int(input("cual es la nota?: "))
comparador = calificación % 10
equalizador = 10 - comparador
if equalizador <= 4:
    resultado = calificación + equalizador
    print(f"tu nota es: {resultado}")
