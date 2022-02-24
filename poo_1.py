"""
poo_1.py
script en python que implemente una clase Figura que como atributo tenga
la cantidad de lados.

una vez creada la clase crear dos figuras (objetos) y mostrar su cantidad de
lados
"""
class Figura:
    def __init__(self):
        self._lados = None

    @property #getter de lados
    def lados(self):
        return self._lados
    @lados.setter #setter del atributo
    def lados(self, valor):
        if valor < 3:
            print("valor debe ser mayor que 3")
            self._lados = None
        else:
            self._lados = valor

    @lados.deleter
    def lados(self):
        del self._lados

def main():
    triangulo = Figura()
    cuadrado = Figura()
    triangulo.lados = -3
    cuadrado.lados = 4
    print(f"Triangulo tiene {triangulo.lados} lados")
    print(f"Cuadrado tiene {cuadrado.lados} lados")

if __name__ == "__main__":
    main()
