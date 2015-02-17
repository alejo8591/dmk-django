from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from order.models import Order, Customer, Product, Stock
from order.forms import CustomerForm, ProductForm, StockForm, OrderForm

def order_index(request):

    context = {}

    orders = Order.objects.all()

    context.update({'orders':orders, 'title': 'Listado de Ordenes'})

    #return render(request, 'order/index.html', context)
    return render(request,'order_index.html', context)


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

        context.update({'product':product,'title': 'Detalle del Cliente'})
        try:
            stock = Stock.objects.get(stock_product_id=product_id)

            context.update({'stock':stock})

        except Stock.DoesNotExist:

            context.update({'error_stock':True})

    except Product.DoesNotExist:
        context.update({'error': True})

    return render(request, 'product_detail.html', context)


""" Creacion de elementos """

def add_customer(request):

    context = {}

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():
            
            form.save()

            return redirect(order_index)

        else:
            print(form.errors)

    else:
        context.update({'form': CustomerForm()})
    return render(request, 'add_customer.html',context)


def add_product(request):

    context = {}

    if request.method == 'POST':

        product_form = ProductForm(request.POST, prefix='product')
        stock_form = StockForm(request.POST, prefix='stock')

        if product_form.is_valid() and stock_form.is_valid():

            product_save = product_form.save()

            stock_save = stock_form.save(commit=False)

            stock_save.stock_product_id = product_save

            stock_save.save()

            return redirect(order_index)

        else:
            print(form.errors)

    else:
        context.update({'product_form': ProductForm(prefix='product'), 'stock_form': StockForm(prefix='stock')})

    return render(request, 'add_product.html',context)


def add_order(request):

    context = {}

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(order_index)
        else:
            print(form.errors)

    else:
        context.update({'form':OrderForm()})

    return render(request, 'add_order.html', context)


""" Lista de elementos """

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


""" Actualizacion de elementos """

def customer_edit(request, customer_id):

    context = {}

    try:
        customer = get_object_or_404(Customer, id=customer_id)

        if request.method == 'POST':

            form = CustomerForm(request.POST)

            if form.is_valid():
                customer.customer_name = form.cleaned_data['customer_name']
                customer.customer_address = form.cleaned_data['customer_address']
                customer.customer_phone = form.cleaned_data['customer_phone']

                customer.save()

                return HttpResponseRedirect('/order/customer/detail/%s/' % customer.customer_slug)

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
        product = get_object_or_404(Product, id=product_id)
        stock = get_object_or_404(Stock, id=stock_id)

        if request.method == 'POST':

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

                """
                    product_update = product_form.save()

                    stock_update = stock_form.save(commit=False)

                    stock_update.stock_product_id = product_update

                    stock_update.save()
                """

                return HttpResponseRedirect('/order/product/detail/%s/' % product.id)

        else:
            stock_data = {
                'stock_quantity': stock.stock_quantity
            }

            product_data = {
                'product_name': product.product_name,
                'product_type': product.product_type,
                'product_price': product.product_price,
                'product_description': product.product_description
            }

            product_form = ProductForm(initial=product_data, prefix='product')
            stock_form = StockForm(initial=stock_data, prefix='stock')

    except Customer.DoesNotExist:

        context.update({'error': True})

    context.update({
        'title': 'Editar Cliente',
        'product_form': product_form,
        'stock_form': stock_form,
        'update': True,
        'product': product,
        'stock': stock})

    return render(request, 'add_product.html', context)


def order_edit(request, order_id):

    context = {}

    try:
        order = get_object_or_404(Order, id=order_id)

        if request.method == 'POST':

            form = OrderForm(request.POST)

            if form.is_valid():
                order.order_customer_id = form.cleaned_data['order_customer_id']
                order.order_product_id = form.cleaned_data['order_product_id']
                order.order_amount = form.cleaned_data['order_amount']

                order.save()

                return HttpResponseRedirect('/order/detail/%s/' % order.id)

        else:
            order_data = {
                'order_product_id': order.order_product_id,
                'order_customer_id': order.order_customer_id,
                'order_amount': order.order_amount
            }

            form = OrderForm(initial=order_data)

    except Order.DoesNotExist:

        context.update({'error': True})

    context.update({'title': 'Editar Cliente', 'form': form, 'update': True, 'order': order})

    return render(request, 'add_order.html', context)