# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:55:11 2024

@author: FORMACION
Jhonny Torres alias Jhonky"__________"
"""

class Libro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def get_autor_completo(self):
        return f"{self.autor.nombre}"

class Autor:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

# Ejemplo de uso

autor1 = Autor(1, "Antoine de Saint-Exupéry")
autor2 = Autor(2, "Gabriel García Márquez")

libro1 = Libro(1, "El Principito", autor1)
libro2 = Libro(2, "Cien años de soledad", autor2)

print(f"Libro 1: {libro1.titulo}")
print(f"Autor: {libro1.get_autor_completo()}")

print(f"Libro 2: {libro2.titulo}")
print(f"Autor: {libro2.get_autor_completo()}")

        
        