"""
anidamiento_estructural.py
script en el que se le solicita al usuario que responda unas preguntas
en caso de responder bien avanza, en caso de responder mal, pierde y se termina el juego
"""

print("bienvenido/a pongamos a prueba tu conocimiento:")

res = int(input("cual es la velocidad de la luz en m/s?: "))
if res == 299792458:
    print("bien capo, correcto!")
    res = int(input("cuanto es 8+8/8*8?: "))
    if res == 8+8/8*8:
        print("bien capo, al que sigue")
        res = input("que color eran las mangas del chaleco de napoleon? ")
        if res == "los chalecos no tienen mangas":
            print("bien capo ganaste")
        else:
            print("al lobby gordo")
    else:
        print("lo siento respuesta incorrecta")
else:
    print("lo siento respuesta incorrecta")
