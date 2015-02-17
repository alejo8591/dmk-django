# -*- coding: utf-8 -*-

from numpy import hypot, sqrt

class Figures(object):
	__slots__ = ('dim1', 'dim2')

	def __init__(self, dim1, dim2):
		self.dim1 = dim1
		self.dim2 = dim2
		
	def area(self):
		print('El aréa de la figura no esta definida.')

class Triangle(Figures):
	
	def __init__(self, dim1, dim2, base, height):
		super().__init__(dim1, dim2)
		self.base = base
		self.height = height

	def area(self):
		print('El área del tríangulo es: ')
		return((self.base * self.height) / 2)

	def perimeter(self):
		print('El perimetro del tríangulo es: ')
		return(self.dim1 + self.dim2 + self.base)

	def hypotenuse(self):
		print('La hipotenusa es: ')
		return(hypot(self.base, self.height))


def main():
	F = Figures(10, 10)
	T = Triangle(10, 10, 5, 6)

	print(T.area())
	print(T.perimeter())
	print(T.hypotenuse())

if __name__ == '__main__':
	main()













