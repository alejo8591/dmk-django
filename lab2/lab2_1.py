# -*- coding: utf-8 -*-
"""
Program: lab2_1.py
Author: Alejandro Romero

Calcuar la tasa de impuesto de un alimento

1. Declaracion de variables:
	      tax tasa de impuesto
	      tax_one tasa de impuesto adicional

2. Entradas:
          valor del alimento
          numero de alimentos

3. Computacion:
		  tasa de entrada = suma de numero de alimentos + tax + tax_one

4. Salida:
	El calculo de los elementos comprados

"""

# Declaracion de Constantes
TAX = 0.16
TAX_ONE = 0.03


# Entrada(s) del teclado
food = int(input('Ingrese el valor del Alimento: '))

ammount_food = int(input('Ingrese la cantidad de Alimentos: '))

# Computaciones

total = (food * ammount_food) * (TAX + TAX_ONE)

print("El total de los alimentos es:", total)

