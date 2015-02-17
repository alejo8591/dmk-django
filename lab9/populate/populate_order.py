import os, sys, inspect
"""
En esta linea de codigo nos ubicamos a nivel de proyecto para que encuentre los modulos
que le vamos a indicar
"""
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import lab7

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab7.settings')

"""
Importando los modelos de la aplicacion "order"
"""
from order.models import Customer, Product, Stock, Order
"""
Preparando el script para trabajar con un entorno de config Django
"""
import django
django.setup()

"""
Funcion para crear los datos en la base de datos 
"""

def populate():

	customer_one = add_customer(
		customer_name='Alejandro Romero',
		customer_address='Cr 20 # 30 - 30',
		customer_phone='3383838')

	product_one = add_product(
		product_name='Citizen #1',
		product_price=690455.33,
		product_type='Reloj',
		product_description='Reloj')

	stock_one = add_stock(
		stock_product_id=product_one,
		stock_quantity=30)

	order_one = add_order(
		order_customer_id=customer_one,
		order_product_id=product_one,
		order_amount=4)

	for product in Product.objects.all():
		for stock in Stock.objects.filter(stock_product_id=product):
			print("El producto {0} tiene un stock de {1} unidades".format(str(product), str(stock.stock_quantity)))


	for customer in Customer.objects.all():
		for order in Order.objects.filter(order_customer_id=customer):
			print("El cliente {0} tiene una orden con #{1}".format(str(customer), str(order.id)))

def add_customer(**kwargs):
	customer = Customer.objects.get_or_create(
		customer_name=kwargs['customer_name'], 
		customer_address=kwargs['customer_address'],
		customer_phone=kwargs['customer_phone'])[0]

	return customer

def add_product(**kwargs):
	product = Product.objects.get_or_create(
		product_name=kwargs['product_name'],
		product_price=kwargs['product_price'],
		product_type=kwargs['product_type'],
		product_description=kwargs['product_description'])[0]
	
	return product

def add_stock(**kwargs):
	stock = Stock.objects.get_or_create(
		stock_product_id=kwargs['stock_product_id'],
		stock_quantity=kwargs['stock_quantity'])[0]

	return stock

def add_order(**kwargs):
	order = Order.objects.get_or_create(
		order_customer_id=kwargs['order_customer_id'],
		order_product_id=kwargs['order_product_id'],
		order_amount=kwargs['order_amount'])[0]

	return order

if __name__ == 'main':
	print('Creando info en la BD')
	populate()

