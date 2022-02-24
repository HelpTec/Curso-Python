"""
archivos_2.py

script en python que me muestre todos los nombres de los archivos contenidos en
una carpeta y que contengan una cierta extensión
"""
import pathlib

ruta = pathlib.Path(r"C:\Users\Admin\Desktop\curso de python\Apendice")

for archivo in ruta.glob("*.txt"):
    print(archivo)
