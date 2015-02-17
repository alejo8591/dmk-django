from order.models import Customer, Product, Stock, Order
from autofixture import generators, register, AutoFixture

import random

types = random.choice(('Hardware', 'Software', 'Test Software', 'Test Hardware', 'Apps', 'Big Data',))
products = random.choice(('Casio 33W', 'Lumia 34', 'Cable USB', 'Quanta 4G', 'Magic Mouse', 'Moto G', 'Moto X',))

""" Clase para crear informacion para el modelo Customer """
class CustomerFixture(AutoFixture):
	field_values = {
		'customer_name': generators.FirstNameGenerator(),
		'customer_address': generators.SmallIntegerGenerator(min_value=1240, max_value=9999),
		'customer_phone': generators.IntegerGenerator(min_value=124000, max_value=9999999)
	}

class ProductFixture(AutoFixture):
	field_values = {
		'product_name': generators.StaticGenerator(products),
		'product_price': generators.PositiveIntegerGenerator(),
		'product_type': generators.random.choice(types),
		'product_description': generators.LoremGenerator()
	}

class StockFixture(AutoFixture):
	field_values = {
		'stock_quatity': generators.SmallIntegerGenerator(min_value=1240, max_value=9999)
	}

class OrderFixture(AutoFixture):
	field_values = {
		'order_amount': generators.SmallIntegerGenerator(min_value=1, max_value=10)
	}

""" Asociando modelo a clase para generar informacion """
register(Customer, CustomerFixture)
register(Product, ProductFixture)
register(Stock, StockFixture)
register(Order, OrderFixture)