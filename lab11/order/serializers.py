from rest_framework import serializers
from order.models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ('customer_name', 'customer_slug', 'customer_address', 'customer_phone', 'url',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('product_name', 'product_type', 'product_description', 'product_price', 'id', 'url',)


class StockSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Stock
		fields = ('stock_product_id', 'id', 'stock_quantity', 'url',)


class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ('order_customer_id', 'order_product_id', 'order_amount', 'id', 'url',)