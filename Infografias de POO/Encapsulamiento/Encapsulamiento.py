# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 01:45:22 2024

@author: Jhonny Torres alias Jhonky"__________"
"""

class Persona:
    
    # Atributo privado
    __edad = 20
    
    # Metodo público
    def mostrar_edad(self):
        return self.__edad
    
    
    
 
persona = Persona()
print(persona.mostrar_edad())