"""
listas_e.py
script en python que implemente el clasico juego de "ahorcado".
el juego consiste en que el usuario intente adivinar una palabra
secreta de la cual inicialmente solo se le muestra la cantidad
de letras que contiene. Para esta versión del juego, el usuario
deberá intentar adivinar el nombre de alguno de los 35 paises
que conforman el continente americano.

El juego debe comenzar seleccionando de forma aleatoria el
nombre de alguno de los paises; dichos nombres deberán estar
almacenados en una lista. una vez seleccionado el país, se le mostrará al
usuario una cadena formada por tantos guiones bajos
como letras y espacios en blanco haya en el nombre del país.
por ejemplo si el país es "Cuba", al usuario se le mostraría
"____" (4 guiones bajos).

A partir de ahí el usuario debe intentar adivinar las letras
que conforman el nombre teniendo hasta 5 oportunidades para
fallar. si el usuario propone una letra y existe en el nombre
del país, entonces todas las ocurrencias de esa letra se
reemplazan en la palabra secreta; por ejemplo para la palabra
"Cuba", si el usuario propusiera la "a" entonces la palabra
secreta se actualizaría para mostrar "___a".

El juego termina si se han descubierto todas las letras del
nombre o el usuario se ha equivocado 6 veces.
"""
import random
import os

PAISES = ['Antigua y Barbuda','Argentina','Bahamas','Barbados',
'Belice','Bolivia','Brasil','Canadá','Chile','Colombia',
'Costa Rica','Cuba','Dominica','Ecuador','El Salvador',
'Estados Unidos','Granada','Guatemala','Guyana','Haití',
'Honduras','Jamaica','México','Nicaragua','Panamá','Paraguay',
'Perú','República Dominicana','San Cristóbal y Nieves',
'San Vicente y las Granadinas','Santa Lucía','Surinam',
'Trinidad y Tobago','Uruguay','Venezuela']



def titulo(vidas):
        print("""           JUEGO DEL AHORCADO DE PENETRÓN
        ADIVINA EL PAÍS, TENES 5 VIDAS, POR CADA ERROR TE DESCUENTO UNA
        SI TE QUEDAS SIN VIDAS SERÁS ELIMINADO""")
        print(f"""
        VIDAS: {vidas}""")

def secreteador():
    pais = random.choice(PAISES)
    guionizador = '_'*len(pais)
    return pais, guionizador

def reemplezar_simbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos]+simbolo+secreto[pos+1:]
        inicio = pos + 1
    return secreto

def main(PAISES):
    original, secreto = secreteador()
    continuar = True
    vidas = 5
    while continuar:
        os.system("cls")
        titulo(vidas)
        print(f'Palabra: {secreto}')
        s = input('¿Cuál símbolo quieres destapar? ')
        if s in original:
            secreto = reemplezar_simbolo(original, secreto, s)
            if secreto == original:
                continuar = False
                print("ganaste")
                input("enter")
        else:
            vidas = vidas - 1
            if vidas == 0:
                continuar = False
                print("perdiste")
                print(f"{original}")
        input("stop")

main(PAISES)
