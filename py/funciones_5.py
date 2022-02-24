"""
funciones_5.py
script en python que implemente una función que haga el calculo del
imc del usuario. la función debe recibir el peso y la estatura del
usuario y como resultado regresa el valor del indice de masa corporal.
"""
def imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("indique su peso: "))
altura = float(input("indique su altura: "))

print(f"tu imc es {imc(peso, altura) : .2f}")
