"""
archivos_3.py
scripts en python que busque un archivo en una carpeta e indique si existe o no.
En caso de existir mostrará su tamaño
"""
import pathlib

ruta = pathlib.Path(".")

buscar = input("ingrese nombre completo del archivo a buscar: ")

buscar = ruta / buscar

if buscar.exists():
    print(f"El archivo existe y mide {buscar.stat().st_size} bytes")
else:
    print("el archivo no existe")
