"""
repetitiva_mientras_e.py

vamos a hacer dos jugadores, un jugador maquina y un jugador usuario. el primero que adivine gana
la regla es basica. el numero será entre 1 y 100. será por turnos, el jugador
inicia y deberá decir un numero, si no es, la maquina indicará que el numero es
mayor o menor.
El jugador maquina será "inteligente" y aprenderá de los errores propios y del
jugador, va a utilizar los datos arrojados para adivinar que numero es

el primero que acierta gana
"""
import random
import os

def ipnumber(pnum):
    print("es mas grande")
    ipnum = pnum
    input("presiona enter para volver a intentar")
    return ipnum

def pnumber(ipnum, spnum):
    pnum = random.randint(ipnum, spnum)
    print(f"PENETRÓN dice {pnum}")
    return pnum

def spnumber(pnum):
    print("es mas chico")
    spnum = pnum
    input("presiona enter para volver a intentar")
    return spnum



SECRETO = random.randint(1, 100)
num = 0
pnum = 0
ipnum = 0
spnum = 100

def enojo():
    print("PENETRÓN DICE: ¿ACASO QUERES MAREARME?")

def enojo_2():
    print("PENETRÓN DICE: PRESTA ATENCIÓN O TE VOY A GANAR")

def enojo_3():
    print("PENETRÓN DICE: NO ME COPIES!!")

while SECRETO != num and SECRETO != pnum:
    os.system("cls")
    print("""===================================================================
                                ADIVINA EL NUMERO SECRETO
                    "elige un numero del 1 al 100 y ganale a PENETRÓN"
===============================================================================
""")
    num = int(input("tu turno: "))
    if SECRETO != num:
        if SECRETO > num:
            print("pensá en uno mas grande")
            if SECRETO > num and num == ipnum:
                enojo_3()
                pnum = pnumber(ipnum, spnum)
                if SECRETO < pnum:
                    spnum = spnumber(pnum)
                elif SECRETO > pnum:
                    ipnum = ipnumber(pnum)
            elif SECRETO > num and num < ipnum:
                enojo()
                pnum = pnumber(ipnum, spnum)
                if SECRETO < pnum:
                    spnum = spnumber(pnum)
                elif SECRETO > pnum:
                    ipnum = ipnumber(pnum)
            elif SECRETO > num and num > ipnum:
                ipnum = num+1
                pnum = pnumber(ipnum, spnum)
                if SECRETO < pnum:
                    spnum = spnumber(pnum)
                elif SECRETO > pnum:
                    ipnum = ipnumber(pnum)
        elif SECRETO < num:
            print("pensá en uno mas chico")
            if SECRETO < num and num == spnum:
                    enojo_3()
                    pnum = pnumber(ipnum, spnum)
                    if SECRETO < pnum:
                        spnum = spnumber(pnum)
                    elif SECRETO > pnum:
                        ipnum = ipnumber(pnum)
            elif SECRETO < num and num > spnum:
                    enojo_2()
                    pnum = pnumber(ipnum, spnum)
                    if SECRETO < pnum:
                        spnum = spnumber(pnum)
                    elif SECRETO > pnum:
                        ipnum = ipnumber(pnum)
            elif SECRETO < num and num < spnum:
                spnum = num-1
                pnum = pnumber(ipnum, spnum)
                if SECRETO < pnum:
                    spnum = spnumber(pnum)
                elif SECRETO > pnum:
                    ipnum = ipnumber(pnum)
else:
    if SECRETO == pnum:
        print("PENETRÓN TE HA DERROTADO")
    elif SECRETO == num:
        print("DERROTASTE A PENETRÓN")
