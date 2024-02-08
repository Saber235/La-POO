# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

class Persona:

    # Atributos
    edad = None
    nombre = None

    # Constructor
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre


# Crear una instancia
persona = Persona(20, "Juan")

# Acceder a los atributos
print(persona.edad)
print(persona.nombre)