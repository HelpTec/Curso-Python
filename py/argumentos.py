"""
argumentos.py
script en python que implemente un procedimiento para imprimir un menú
generico. el procedimiento deberá recibir el titlo del menu como
primer argumento, seguido de las opciones a imprimir y finalmente un
parametro con nombre para el mensaje de error en caso de una opción
no valida
"""

def menu(titulo, *args, **kwargs):
    print(f"""                      {titulo}""")
    for x in range(len(args)):
        print(f"{x+1}){args[x]}")
    opc = int(input("selecciona una opción: "))
    if 1 <= opc <= len(args):
        print(f"seleccionaste la opción {args[opc-1]}")
    else:
        print("opción no valida")
        if "error" in kwargs:
            print(f'{kwargs["error"]}')

menu("operaciónes aritmeticas", "suma", "resta", "multiplicación", "división",
"tu vieja", error="no existe tal opción")

print("adios")
