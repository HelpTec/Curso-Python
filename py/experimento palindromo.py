"""
script de experimento para hacer un comprobador de palindromos
letra6 = filtro[5:6]
letra6 = ord(letra6)
letra5 = ord(letra5)
letra1 = ord(letra1)
letra4 = ord(letra4)
letra3 = ord(letra3)
letra2 = ord(letra2)
comprobador = (letra1*100000000)+(letra2*1000000)+(letra3*10000)+(letra4*100)+letra5
inversor = (letra5*100000000)+(letra4*1000000)+(letra3*10000)+(letra2*100)+letra1
filtro = palabra.upper()
"""
import os
CONTINUAR = True

while CONTINUAR:
    os.system("cls")
    palabra = input("ingrese su palabra o escriba SALIR para terminar: ")
    contador = len(palabra)
    if palabra == "SALIR":
        CONTINUAR = False
    elif contador <= 2:
        print("tu palabra no es un palindromo")
        input("presione enter para continuar")
    elif contador == 3:
        letra1 = palabra[0:1]
        letra2 = palabra[1:2]
        letra3 = palabra[2:3]
        inversor = letra3+letra2+letra1
        if palabra == inversor:
            print("tu palabra es un palindromo")
            input("presione enter para continuar")
        else:
            print("no es un palindromo")
            input("presione enter para continuar")
    elif contador == 4:
        letra1 = palabra[0:1]
        letra2 = palabra[1:2]
        letra3 = palabra[2:3]
        letra4 = palabra[3:4]
        inversor = letra4+letra3+letra2+letra1
        if palabra == inversor:
            print("tu palabra es un palindromo")
            input("presione enter para continuar")
        else:
            print("no es un palindromo")
            input("presione enter para continuar")
    elif contador == 5:
        letra1 = palabra[0:1]
        letra2 = palabra[1:2]
        letra3 = palabra[2:3]
        letra4 = palabra[3:4]
        letra5 = palabra[4:5]
        inversor = letra5+letra4+letra3+letra2+letra1
        if palabra == inversor:
            print("tu palabra es un palindromo")
            input("presione enter para continuar")
        else:
            print("no es un palindromo")
            input("presione enter para continuar")
    elif contador == 6:
        letra1 = palabra[0:1]
        letra2 = palabra[1:2]
        letra3 = palabra[2:3]
        letra4 = palabra[3:4]
        letra5 = palabra[4:5]
        letra6 = palabra[5:6]
        inversor = letra6+letra5+letra4+letra3+letra2+letra1
        if palabra == inversor:
            print("tu palabra es un palindromo")
            input("presione enter para continuar")
        else:
            print("no es un palindromo")
            input("presione enter para continuar")
    elif contador == 6:
        letra1 = palabra[0:1]
        letra2 = palabra[1:2]
        letra3 = palabra[2:3]
        letra4 = palabra[3:4]
        letra5 = palabra[4:5]
        letra6 = palabra[5:6]
        letra7 = palabra[6:7]
        inversor = letra7+letra6+letra5+letra4+letra3+letra2+letra1
        if palabra == inversor:
            print("tu palabra es un palindromo")
            input("presione enter para continuar")
        else:
            print("no es un palindromo")
            input("presione enter para continuar")
    elif contador >= 7:
        print("""PENETRÓN DICE: Perdón, el gordo que me programó es muy vago para
y no me codeo para que vea tantas letras...""")
        input("presione enter para continuar")
    else:
        print("no es un palindromo")
        input("presione enter para continuar")
