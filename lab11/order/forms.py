from django import forms
from order.models import Customer, Product, Stock, Order


class CustomerForm(forms.ModelForm):

	customer_name = forms.CharField(max_length=128, help_text='Nombre del Cliente')
	customer_address = forms.CharField(max_length=64, help_text='Dir. del Cliente')
	customer_phone = forms.CharField(max_length=24, help_text='Tel. del Cliente')

	class Meta:
		model = Customer
		fields = ('customer_phone', 'customer_address', 'customer_name',)
		excludes = ('date_created_customer', 'date_updated_customer',)


class ProductForm(forms.ModelForm):

	product_name = forms.CharField(max_length=128, help_text='Nombre del Producto')
	product_price = forms.DecimalField(max_digits=64, 
		decimal_places=2, 
		help_text='Precio del Producto', 
		initial=0)
	product_type = forms.CharField(max_length=64, help_text='Tipo de Producto')
	product_description = forms.CharField(widget=forms.Textarea, help_text='Descripcion del Producto')

	class Meta:
		model = Product
		fields = ('product_name', 'product_price', 'product_type', 'product_description',)


class StockForm(forms.ModelForm):
	stock_quantity = forms.IntegerField(help_text='Ingrese el Stock del Product', initial=0)

	class Meta:
		model = Stock
		fields = ('stock_quantity',)
		excludes = ('stock_product_id',)


class OrderForm(forms.ModelForm):

	order_customer_id = forms.ModelChoiceField(queryset=Customer.objects.all(),
						help_text='Seleccione el Cliente')

	order_product_id = forms.ModelChoiceField(queryset=Product.objects.all(),
					    help_text='Seleccione el Producto')

	order_amount = forms.DecimalField(help_text='Cantidad del Producto', initial=0)

	class Meta:
		model = Order
		fields = ('order_customer_id', 'order_product_id', 'order_amount',)
