# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:48:14 2023

@author: USUARIO
"""

# Ejemplo de un atributo privado
class Persona:
    # Atributo privado
    _nombre = "Juan Pérez"

    # Método para obtener el nombre
    def get_nombre(self):
        return self._nombre

    # Método para establecer el nombre
    def set_nombre(self, nombre):
        self._nombre = nombre


# Ejemplo de uso del atributo privado
persona = Persona()

# Obtenemos el nombre de la persona
nombre = persona.get_nombre()
print(nombre)

# Establecemos el nombre de la persona
persona.set_nombre("Pedro Rodríguez")
nombre = persona.get_nombre()
print(nombre)
