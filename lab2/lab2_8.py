# -*- coding: utf-8 -*-

class A(object):
	def __init_(self):
		print("A")
		super(A, self).__init__()

class B(A):
	def __init__(self):
		print("B")
		super(B, self).__init__()

class C(A):
	def __init__(self):
		print("C")
		super(C, self).__init__()

class D(C, B):
	def __init__(self):
		print("D")
		super(D, self).__init__()


print("__mro__:", [x.__name__ for x in D.__mro__])

instance = D()


