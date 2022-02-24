"""
pila_1.py
script en Python que solicite al usuario escribir una expresión
aritmetica y el programa le indique si dicha expresión esta
balanceada, es decir, si tiene la misma cantidad de parentesis
de apertura y de cierre
"""
def validar_expresion(expresion):
    pila = []
    for simbolo in expresion:
        if simbolo == "(":
            pila.append("(")
        elif simbolo == ")":
            if len(pila) > 0:
                pila.pop()
            else:
                return False
        return len(pila) == 0

def main():
    print("""escribe una expresión aritmetica y te digo si esta balanceada
    con respecto a parentesis""")
    e = input("expresión: ")
    valida = validar_expresion(e)
    if valida:
        print("su expresión esta balanceada")
    else:
        print("la expresión no esta balanceada")
    print("nos vemos")
    input("presione enter")

main()
