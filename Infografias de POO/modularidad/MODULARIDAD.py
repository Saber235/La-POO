# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:37:48 2023

@author: USUARIO
"""
class FiguraGeometrica:
    def __init__(self, color):
        self.color = color

    def dibujar(self):
        print("La figura geométrica es de color {}".format(self.color))


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def dibujar(self):
        print("El cuadrado es de color {}".format(self.color))


def main():
    figura = FiguraGeometrica("azul")
    cuadrado = Cuadrado(5, "rojo")

    figura.dibujar()
    cuadrado.dibujar()


if __name__ == "__main__":
    main()