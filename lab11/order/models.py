#-*- encoding:utf-8 -*-
from django.db import models
import datetime
from django.utils.text import slugify

class Customer(models.Model):
	customer_name = models.CharField(max_length=128, 
		blank=True, null=True, 
		verbose_name='Nombre', 
		help_text='Ingrese el Nombre Completo.')

	customer_slug = models.SlugField(max_length=128, blank=True, null=True)
	
	customer_address = models.CharField(max_length=64, 
		blank=True, null=True,
		verbose_name='Direccion', 
		help_text='Ingrese la Direccion del Cliente.')

	customer_phone = models.CharField(max_length=24, 
		blank=True, null=True,
		verbose_name='Telefono', 
		help_text='Ingrese el teléfono del Cliente.')

	""" Campos para auditar el cliente con respecto a la creacion y la actualizacion """
	date_created_customer = models.DateTimeField(auto_now=True)
	date_updated_customer = models.DateTimeField()

	def save(self, *args, **kwargs):
		# Tomando la info del tiempo en ese instante
		date = datetime.datetime.now()

		self.date_updated_customer = date

		self.customer_slug = slugify(self.customer_name)

		super(Customer, self).save(*args, **kwargs)

	def __str__(self):
		return self.customer_name


class Product(models.Model):
	product_name = models.CharField(max_length=128, 
		blank=True, null=True, 
		verbose_name='Producto', 
		help_text='Ingrese el Nombre del Producto.')

	product_price = models.DecimalField(max_digits=64,
		decimal_places=2,
		verbose_name='Precio',
		help_text='Precio del Producto')

	product_type = models.CharField(max_length=128, 
		blank=True, null=True, 
		verbose_name='Tipo de Producto', 
		help_text='Ingrese el Tipo de Producto al que pertence.')

	product_description = models.TextField(max_length=400,
		verbose_name='Descripción del Producto', 
		help_text='Ingrese la Descripción del Producto.')


	product_likes = models.IntegerField(null=True, blank=True, default=0)

	def __str__(self):
		return self.product_name


class Stock(models.Model):
	stock_product_id = models.ForeignKey('Product')
	stock_quantity = models.IntegerField(max_length=24,
		verbose_name='Cantidad del Producto',
		help_text='Ingrese la Cantidad de Producto Disponible')

	def __str__(self):
		return self.stock_product_id.product_name


class Order(models.Model):
	order_customer_id = models.ForeignKey('Customer')
	order_product_id = models.ForeignKey('Product')
	order_amount = models.IntegerField(max_length=64)
	order_date = models.DateField(auto_now=True)

	def __str__(self):
		return self.order_product_id.customer_name
