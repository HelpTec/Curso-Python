"""
archivos_4.py
script en python que muestre todos los tipos de archivos que hay en una carpeta

"""
import pathlib

def main():
    ruta = pathlib.Path(".")

    extensiones = {archivo.suffix for archivo in ruta.iterdir()}
    print(f"extensiones: {extensiones}")

if __name__ == "__main__":
    main()
