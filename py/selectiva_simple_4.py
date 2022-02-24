"""
selectiva_simple_4.py
este script solicitará al usuario una temperatura y de esta esta misma
dentro de sus rangos establecidos devolverá un mensaje diciendo que esta bien
"""
temperatura = float(input("buenos días! que temperatura hace?: "))
if temperatura >= 18 and temperatura <= 23:
    print("tenemos un buen clima!")
if temperatura <= 17:
        print("hace bastante frio, abrigate")
if temperatura >= 24:
        print("hace mucho calor, hidratate")
print("fin del script")
