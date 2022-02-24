"""
selectiva_simple_2.py
pedirle a python que genere un numero aleatorio entre 1 y 10 y que
el usuario adivine. si adivina que lo felicite
"""
#agrega el modulo random al programa atraves del comando import
import random
secreto = random.randint(1, 5)
usuario = input("hola, ¿como te llamas?: ")
print(f"hola {usuario} vamos a jugar algo facil")
print("estoy pensando en un numero del 1 al 5")
adivinanza = int(input("decime que numero estoy pensando: "))
if secreto == adivinanza:
    print(f"bien {usuario}!!!! adivinaste")
    print("logro desbloqueado: ADIVINADOR MISTICO")
if secreto != adivinanza:
    print(f"uuuuh {usuario} no es ese... probá denuevo despues...")
    print(f"el numero secreto era {secreto}... buena suerte la proxima!!")
