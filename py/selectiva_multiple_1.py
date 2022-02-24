"""
selectiva_multiple_1.py
script para instrucción selectiva multiple
script que confirma si calificación y cantidad de asistencias son correctas para
felicitar al usuario. en caso contrario se le indicara en que falló
"""
usuario = input("hola, decime tu nombre de usuario: ")
print(f"Hola {usuario}, vamos a ver si aprobaste tu curso de programación!")
calificación = int(input("ingresanos tu calificación final: "))
asistencias = int(input("ahora la cantidad de días cursados: "))
redondeo = int(calificación % 10)
if redondeo >= 6:
    calificación = 10 - redondeo + calificación
    print(f"tu calificación final es {calificación}")
if calificación >= 70 and asistencias >= 10:
    print(f"felicidades {usuario}!!! aprobaste tu curso!!!")
elif calificación < 70 and asistencias >= 10:
    print(f"tu nota fué lo que no alcanzó {usuario}")
elif calificación >= 70 and asistencias < 10:
    print(f"tus notas estan bien {usuario} pero faltaste a muchas clases...")
elif calificación < 70 and asistencias < 10:
    print(f"siquiera empezaste el curso {usuario}?? volvé a hacerlo todo")
else:
    print(f"la posta {usuario} no tengo idea que pasó flaco")
print("fin del script")
