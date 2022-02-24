import os
import queue

AGENDAR = 1
ATENDER = 2
SALIR = 0

def menu():
    os.system("cls")
    print(f"""                   AGENDAR
    {AGENDAR}) AGENDAR
    {ATENDER}) ATENDER
    {SALIR}) SALIR""")


def agendar(agenda):
    print(f"""      AGENDAR EVENTO      """)
    evento = input("Evento: ")
    agenda.put(evento)

def atender(agenda):
    print(f"""      ATENDER EVENTO      """)
    if agenda.empty():
        print("NO HAY EVENTOS QUE ATENDER")
        input("presione enter para continuar")
    else:
        evento = agenda.get()
        print(f"Evento: {evento} será atendido")

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        menu()
        opc = int(input("Selecciona una opción: "))
        os.system("cls")
        if opc == AGENDAR:
            agendar(agenda)
        elif opc == ATENDER:
            atender(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print("Opción no valida")
        input("presiona enter para continuar")
    input("Nos vemos")

if __name__ == "__main__":
    main()
