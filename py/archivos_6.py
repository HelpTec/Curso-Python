"""
archivos_6.py
scritp en python que organize el contenido de la carpeta actual de trabajo.
Se deberá generar una carpeta para cada tipo de archivo y todos los archivos
del tipo correspondiente deberan ser movidos a la carpeta según su tipo
"""

import pathlib

def main():
    ruta = pathlib.Path(".")

    diccionario = {k : [v for v in ruta.glob(f"*{k}")]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}

    for extension, archivos in diccionario.items():
        carpeta = ruta / extension[1:]
        carpeta.mkdir()
        for archivo in archivos:
            archivo.replace(carpeta / archivo.name)

if __name__ == "__main__":
    main()
