"""
archivos_9.py
scripth en python que solicite al usuario una cantidad de peliculas a registrar
y los almacene en un archivo .csv con encabezados para posteriormente
recuperarlos. De cada pelicula se almacenara el titulo, duración y año.
"""

import os
import pathlib
import csv

def registrar(nombre_archivo):
    cantidad = int(input('¿Cuántas películas deseas registrar? '))
    campos = ['Título', 'Duración', 'Año']
    if not pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, "w", newline="") as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=campos)
            writer.writeheader()
    with open(nombre_archivo, "a", newline="") as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        for i in range(cantidad):
            os.system("cls")
            titulo = input("Titulo: ")
            duracion = input("Duración: ")
            anio = input("Año: ")
            writer.writerow({"Título":titulo, "Duración":duracion, "Año":anio})

def recuperar(nombre_archivo):
    os.system("cls")
    print("Peliculas Registradas: ")
    with open(nombre_archivo, "r", newline="") as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for linea in reader:
            for campo, valor in linea.items():
                print(f"{campo}: {valor}")
            print("*"*50)

def main():
    archivo = "Peliculas_csv2"
    registrar(archivo)
    recuperar(archivo)

if __name__ == "__main__":
    main()
