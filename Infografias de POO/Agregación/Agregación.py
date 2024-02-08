# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:46:59 2024

@author: Jhonny Torres alias Jhonky"__________"
"""

class Coche:
    def __init__(self, id, marca, modelo, motor):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

class Motor:
    def __init__(self, id, tipo, potencia):
        self.id = id
        self.tipo = tipo
        self.potencia = potencia

# Ejemplo de uso

motor1 = Motor(1, "V8", 150)
coche1 = Coche(1234, "Toyota", "Corolla", motor1)

print(f"Coche: {coche1.marca} {coche1.modelo}")
print(f"Motor: {coche1.motor.tipo} {coche1.motor.potencia}")
