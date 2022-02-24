"""
procedimiento_main.py
script en python que implemente un procedimiento para saludar al usuario
de manera personalizada; el procedimiento deberá recibir el nombre del
usuario como argumento. se deberá crear otro procedimiento llamado
"main" desde el cual se inicie la ejecución del prorgama y dentro del
cual se solicite el nombre del usuario y se utilice el primer
procedimiento descrito.
"""
def saludo_personalizado(nombre):
    print(f"gusto verte {nombre}")

def main():
    usuario = input("hola como te llamas: ")
    saludo_personalizado(usuario)

if __name__ == "__main__":
    main()
