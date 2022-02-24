"""
selección_selectiva_simple_3.py
este será un script de selección o condición compuesta, tambien veremos/
selección por rangos
"""
asistencias = int(input("cuantos dias de curso tuviste?: "))
nota = int(input("cual fue tu nota?: "))
if asistencias >= 10 and nota >= 7:
    print("felicidades! aprobaste el curso")
    if nota >= 9:
        print("y con nota sobresaliente!")
    if asistencias >= 20:
            print("ademas no faltaste casi nunca!")

print("fin del script")
