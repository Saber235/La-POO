# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 01:56:25 2024

@author: Jhonny Torres alias Jhonky"__________"
"""

class Animal:
    def hacerRuido(self):
        print("Soy un animal")

class Perro(Animal):
    def ladrar(self):
        print("Guau!")

class Gato(Animal):
    def maullar(self):
        print("Miou!")

perro = Perro()
perro.hacerRuido()

perro.ladrar()

gato = Gato()
gato.hacerRuido()

gato.maullar()
