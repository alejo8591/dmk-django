#!/usr/bin/env python
#-*-  coding: utf-8 -*-

"""
Program: lab2_1.py
Author: Alejandro Romero


1. Ingresar el valor para saber el rango:
	
2. Mostrar el tipo de calificacion

"""

number = int(input('Ingrese el numero de su calificación: '))

if number > 89:
	
	letter = 'S'

elif number > 79:

	letter = 'A'

else:
	letter = 'Caso Perdido'

print('Su calificacion esta dentreo del rango: ', letter)