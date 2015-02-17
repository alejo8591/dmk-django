#!/usr/bin/env python
#-*-  coding: utf-8 -*-

decimal = int(input("ingrese el número decimal a Convertir: "))

if decimal == 0:

	print(0)

else:
	print('Resto del cociente binario')
	bstring = ""

	while decimal > 0:
		remainder = float(decimal) % 2
		decimal = float(decimal) // 2
		bstring = str(remainder) + bstring

		print("%5d%8d%10s" % (decimal, remainder, bstring))

	print("La representación binaria es: ", bstring)