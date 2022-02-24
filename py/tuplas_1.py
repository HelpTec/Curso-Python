"""
tuplas_1.py
script en Python que permita almacenar registros de las
mascotas del usuario. Para cada mascota se solicitará el
nombre, la edad, el peso y el tipo de mascota; dichos valores
serán guardados en una tupla. Para permitir la posibilidad de
tener varias mascotas se creara una lista en la cual se guarden
los registros de cada mascota, es decir una lista de tuplas.
El programa deberá contar con un menú ciclico que permita
registrar y consultar las mascotas.
"""
import os
AGENDAR = 0
CONSULTAR = 1
ELIMINAR = 2
SALIR = 3

def Registro(mascotas):
    Nombre = input(f"¿Como se llama tu mascota?: ")
    Edad = int(input(f"Ingresa la edad de {Nombre}: "))
    Peso = float(input(f"Ingresa el peso de {Nombre}: "))
    Tipo = input(f"Ingresa el tipo de mascota que es {Nombre}: ")
    mascotas.append( (Nombre, Edad, Peso, Tipo) )

def Consultar(mascotas):
    if len(mascotas) == 0:
        print("No hay registros...")
    else:
        for mascota in mascotas:
            nombre, edad, peso, tipo = mascota
            print(f"{nombre}")
            print(f"{edad}")
            print(f"{peso}")
            print(f"{tipo}")
            print(f"==="*8)
def main():
    mis_mascotas = []
    mascotas = []
    continuar = True
    while continuar:
        os.system("cls")
        print(f"""               Agenda De mascotas

    {AGENDAR}) AGENDAR
    {CONSULTAR}) CONSULTAR
    {SALIR}) SALIR

    """)
        opc = int(input("Elige una opción: "))
        if opc == AGENDAR:
            os.system("cls")
            Registro(mascotas)
        elif opc == CONSULTAR:
             Consultar(mascotas)
        elif opc == SALIR:
            print("Nos Vemos")
            continuar = False
        else:
            print("opción incorrecta...")
        input("Presiona enter para continuar")

if __name__ == "__main__":
    main()
