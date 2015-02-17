from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from order.models import Order, Customer
from order.forms import CustomerForm, ProductForm, StockForm, OrderForm

""" Vistas de Consulta y detalle de Info """
def index(request):

	context = {}

	orders = Order.objects.all()

	context.update({'orders':orders, 'title': 'Listas de Ordenes'})

	return render(request, 'index.html', context)

def order(request, order_id):
	
	context = {}

	try:
		order = Order.objects.get(id=order_id)

		context.update({'order':order, 'title': 'Detalle de la Orden'})

	except Order.DoesNotExist:
		
		context.update({'error': True})

	return render(request, 'order_detail.html', context)


def customer(request, customer_slug):
	
	context = {}

	try:
		customer = Customer.objects.get(customer_slug=customer_slug)

		context.update({'customer':customer, 'title': 'Detalle del Cliente'})

	except Customer.DoesNotExist:
		
		context.update({'error': True})

	return render(request, 'customer_detail.html', context)


def product(request, product_id):

	context = {}

	try:
		product = Product.objects.get(id=product_id)

		context.update({'product': product, 'title': 'Detalle del Producto'})

		try:

			stock = Stock.objects.get(stock_product_id=product_id)

			context.update({'stock': stock})

		except Stock.DoesNotExist:
		
			context.update({'error_stock': True})

	except Product.DoesNotExist:

			context.update({'error_product': True})

	return render(request, 'product_detail.html', context)

""" Vistas de Creacion y Actualizacion de Info """

def add_customer(request):

	if request.method == 'POST':

		form = CustomerForm(request.POST)

		if form.is_valid():
			# Salvando la informacion en la DB a traves del Modelo
			form.save()

			return redirect(index)

	else:
		context = {'form': CustomerForm()}

	return render(request, 'add_customer.html', context)

def add_order(request):

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(index)
        else:
            print(form.errors)

    else:
        context = {'form':OrderForm()}

    return render(request, 'add_order.html',context)


""" Listados de productos y usuarios """

def customer_list(request):

    context = {}

    customers = Customer.objects.all()

    context.update({'customers':customers, 'title': 'Listado de Clientes'})

    return render(request, 'customer_list.html', context)


def product_list(request):

    context = {}

    products = Product.objects.all()

    context.update({'products':products, 'title': 'Listado de Productos'})

    return render(request, 'product_list.html', context)


 def customer_edit(request, customer_id):
 	context = {}

 	try:
 		customer = get_object_or_404(Customer, id=customer_id)

 		if request.method == 'POST':
 			
 			form = CustomerForm(request.POST)


 			if form.is_valid():

 				customer.customer_name = form.cleaned_data['customer_name']
 				customer.customer_address = form.cleaned_data['customer_address']
 				customer_phone = form.cleaned_data['customer_phone']

 				customer.save()

 				return HttpResponseRedirect('/order/customer/detail/%s/', customer.customer_slug)
 		else:
 			customer_data = {
 				'customer_name': customer.customer_name,
 				'customer_address': customer.customer_address,
 				'customer_phone': customer.customer_phone
 			}

 			form = CustomerForm(initial=customer_data)

 	except Customer.DoesNotExist:
 		context.update({'error': True})

 	context.update({'title': 'Editar Cliente', 'form': form, 'update': True, 'customer': customer})

 	return render(request, 'add_customer.html', context)


def product_edit(request, product_id, stock_id):

	context = {}

	try:
		product = get_object_or_404(Product, id = product_id)
		stock = get_object_or_404(Stock, id = stock_id)

		if  request.method == 'POST':

			product_form = ProductForm(request.POST, prefix='product')
			stock_form = StockForm(request.POST, prefix='stock')

			if product_form.is_valid() and stock_form.is_valid():

				product.product_name = product_form.cleaned_data['product_name']
				product.product_type = product_form.cleaned_data['product_type']
				product.product_price = product_form.cleaned_data['product_price']
				product.product_description = product_form.cleaned_data['product_description']

				stock.stock_quantity = stock_form.cleaned_data['stock_quantity']				

				product.save()
				stock.save()

				return HttpResponseRedirect('/order/product/detail/%s/' % product.id)

		else:
			stock_data = {
				'stock_quantity': stock.stock_quantity
			}

			product_data = {
				'product_name': stock.product_name,
				'product_type': stock.product_type, 
				'product_price': stock.product_price,
				'product_description': stock.product_description
			}

			product_form = ProductForm(product_data, prefix='product')
			stock_form = StockForm(stock_data, prefix='stock')

	except DoesNotExist:

		context.update({'error': True})

	context.update({'title': 'Editar Producto', 'product_form': product_form, 'stock_form': stock_form, 'update': True, 'product': product, 'stock': stock})

	return render(request, 'add_product.html', context)

