def comprobador(palabra):
    reverso = list(reversed(palabra))
    return list(palabra) == reverso

def main():
    continuar = True
    while continuar:
        palabra = input("Ingrese palabra: ")
        if comprobador(palabra):
            print("es un palindromo")
        elif not comprobador(palabra):
            print("no es un palindromo")
        else:
            print("algo salió mal")

if __name__ == "__main__":
    main()
