"""
archivos_1.py

script en python que muestre los nombres de los archivos contenidos en una
carpeta
"""

import pathlib

ruta = pathlib.Path(".")

for archivo in ruta.iterdir():
    print(archivo)
