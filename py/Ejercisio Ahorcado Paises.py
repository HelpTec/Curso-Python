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

def titulo():
    print("""           Juego del ahorcado de Penetron
    Ingresa letras y adivina el país en cuestión
    Si te quedas sin vidas, serás ELIMINADO""")

def secreteador(PAISES):
    pais = random.choice(PAISES)
    guionizador = "_"*len(pais)
    return pais, guionizador

def main(PAISES):
    vidas = 5
    original, secreto = secreteador(PAISES)
    while vidas != 0 and secreto != original:
        os.system("cls")
        titulo()
        print(f"Tu palabra es: {secreto}")
        print(f"Tus vidas restantes: {vidas}")
        letra = input("Elige una letra: ")
        if letra in original:
            cantidad = original.count(letra)
            inicio = 0
            for r in range(cantidad):
                pos = original.find(letra, inicio)
                secreto = secreto[:pos]+letra+secreto[pos+1:]
                inicio = pos+1
        else:
            vidas = vidas-1
            print("Pierdes 1 vida")
            input("Stop")
    else:
        if vidas == 0:
            print("El juego ha terminado, has sido eliminado")
            print(f"La palabra era {original}")
        else:
            print("El juego ha terminado, felicidades!")
            print(f"La palabra era {original}")

main(PAISES)
