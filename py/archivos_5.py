"""
archivos_5.py
script en python que genere un diccionario con las llaves siendo las extensiones
unicas de los archivos encontrados en una carpeta y los valores una lista de
nombres de cada uno de esos archivos
"""
import pathlib

def main():
    ruta = pathlib.Path(".")

    diccionario = {k : [v.name for v in ruta.glob(f"*{k}")]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}

    for extension, archivos in diccionario.items():
        print(f"extensión: {extension}, archivo: {archivos}")

if __name__ == "__main__":
    main()
