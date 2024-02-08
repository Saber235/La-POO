# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:34:41 2023

@author: USUARIO
"""

class Coche:

    # Atributos
    color = None
    marca = None
    modelo = None

    # Métodos
    def arrancar(self):
        print("El coche ha arrancado")

    def acelerar(self):
        print("El coche está acelerando")

    def frenar(self):
        print("El coche está frenando")


# Crear una instancia de la clase Coche
coche = Coche()
coche.color = "rojo"
coche.marca = "Ford"
coche.modelo = "Focus"

# Arrancar el coche
coche.arrancar()

# Acelerar el coche
coche.acelerar()

# Frenar el coche
coche.frenar()