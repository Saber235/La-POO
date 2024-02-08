# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:47:06 2023

@author: USUARIO
"""

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, mi nombre es {}".format(self.nombre))


persona = Persona("Juan")
persona.saludar()
