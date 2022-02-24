"""
archivos_8.py
script en python que solicite al usuario una cantidad de peliculas a registrar
y los almacene en un archivo .csv (Coma Separated Value) para posteriormente
recuperarlos. De cada pelicula se almacenara el titulo, la duración y el año.
"""

import csv
import os

def registrar(nombre_archivo):
    cantidad = int(input("Ingrese cantidad de registros: "))
    with open(nombre_archivo, "a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=",")
        for i in range(cantidad):
            os.system("cls")
            titulo = input("Titulo: ")
            duracion = input("Duración: ")
            anio = input("Año: ")
            writer.writerow([titulo, duracion, anio])

def recuperar(nombre_archivo):
    os.system("cls")
    print("Peliculas registradas: ")
    with open(nombre_archivo, "r", newline="") as archivo_csv:
        reader = csv.reader(archivo_csv)
        for linea in reader:
            print(f"Titulo: {linea[0]}")
            print(f"Duración: {linea[1]}")
            print(f"Año: {linea[2]}")
            print("*"*50)

def main():
    archivo = "peliculas.csv"
    registrar(archivo)
    recuperar(archivo)

if __name__ == "__main__":
    main()
