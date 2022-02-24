"""
funciones_2.py
script en python que implmenete una función encargada de calcular
el indice de masa corporal de un usuario
"""

def imc():
    peso = float(input("indique su peso: "))
    if peso >= 90:
        print("alto gordo, para de morfar")
    else:
        print("bien, continuemos")
    altura = float(input("indique su altura: "))
    indice = peso / (altura ** 2)
    return indice

print("programa que mide tu indice de masa corporal")
i = imc()
print(f"tu imc es {i: .2f}")
if i <= 18.5:
    print("mi pija tiene mas grosor que tu pierna macho")
elif i >= 18.6 and i <= 24.9:
    print("estas bien capo, seguí así")
elif i >= 25:
    if i <= 29.9:
        print("estas entrandole mucho al paty, largalo gordo")
    elif i >= 30 and i <= 34.9:
        print("super obeso fase 1, aflojale a la coca gil")
    elif i >= 35 and i <= 39.9:
        print("""este es el superobeso fase 2, casi no tiene
        pito en toda esa grasa""")
    elif i >= 40:
        print("""man esto ya no es joda, aflojale, asustas y das
        verguenza a tu familia, dormis parado y no te caes gordo virgo""")
else:
    print("algo salió mal creo...")

input("presione enter para continuar")
