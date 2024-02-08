# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 01:29:20 2024

@author: Jhonny Torres alias Jhonky"__________"
"""

class Plato:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self, plato):
        print("{} está comiendo {}.".format(self.nombre, plato.nombre))

plato = Plato("Paella", ["Arroz", "Mariscos", "Verduras"])
persona = Persona("Ana")

persona.comer(plato)
