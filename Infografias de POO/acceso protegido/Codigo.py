# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:21:27 2023

@author: USUARIO
"""

class Persona:
    # Atributo "protegido"
    __edad = 0

    # Método para obtener la edad
    def get_edad(self):
        return self.__edad

    # Método para establecer la edad
    def set_edad(self, edad):
        self.__edad = edad

# Ejemplo de uso
persona = Persona()

# Accedemos a la edad a través de los métodos
edad = persona.get_edad()
print(edad)  # Output: 0

persona.set_edad(25)
edad = persona.get_edad()
print(edad)  # Output: 25


