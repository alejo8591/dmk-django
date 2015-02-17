# -*- coding: utf-8 -*-

"""
File: lab1_9.py

Generador de sentencias aleatoreas con palabras
"""

import random

articles = ('Un', "El", "Ella", "Nosotros", "Yo")

nouns = ("Carro", "Moto", "Avion", "Mujer", "Hombre")

verbs = ("Gustar", "Hablar", "Comer", "Decir")

prepositions = ("con", "por")

def sentences():
	""" Construir y retornar una oración o sentencia """
	return nounPhrase() + " " + verbPhrase() 

def nounPhrase():
	""" Construir y retornar una frase con palabras """
	return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
	""" Construir y retornar una frase con verbo """
	return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
	""" Construir y retornar una preposición a la frase """
	return random.choice(prepositions) + " " + nounPhrase()

def main():
	""" El usuario genera el número de frases a Construir """
	number = int(input("Ingrese el número de frases a Construir: "))
	for count in range(number):
		print(sentences())

"""
a = (1,3,4,4,5,5,4)

b = [1,1,3,3,4,5]

dir(a)

dir(b)

for i in range(1, 40, 2):
	print(i)

for(i = 1; i <= 40; i+2){
	print(i)
}

>>> for i in range(len([1,3,4,4,5])):
...     print(k)

>>> for i in range(len(b)):
...     print(b[i])

"""

main()
