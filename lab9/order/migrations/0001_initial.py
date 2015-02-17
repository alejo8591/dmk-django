# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(null=True, blank=True, max_length=128, verbose_name='Nombre', help_text='Ingrese el Nombre Completo.')),
                ('customer_address', models.CharField(null=True, blank=True, max_length=64, verbose_name='Direccion', help_text='Ingrese la Direccion del Cliente.')),
                ('customer_phone', models.CharField(null=True, blank=True, max_length=24, verbose_name='Telefono', help_text='Ingrese el teléfono del Cliente.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.IntegerField(max_length=64)),
                ('order_date', models.DateField(auto_now=True)),
                ('order_customer_id', models.ForeignKey(to='order.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(null=True, blank=True, max_length=128, verbose_name='Producto', help_text='Ingrese el Nombre del Producto.')),
                ('product_price', models.DecimalField(decimal_places=2, help_text='Precio del Producto', verbose_name='Precio', max_digits=64)),
                ('product_type', models.CharField(null=True, blank=True, max_length=128, verbose_name='Tipo de Producto', help_text='Ingrese el Tipo de Producto al que pertence.')),
                ('product_description', models.TextField(help_text='Ingrese la Descripción del Producto.', max_length=400, verbose_name='Descripción del Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_quantity', models.IntegerField(help_text='Ingrese la Cantidad de Producto Disponible', max_length=24, verbose_name='Cantidad del Producto')),
                ('stock_product_id', models.ForeignKey(to='order.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='order_product_id',
            field=models.ForeignKey(to='order.Product'),
            preserve_default=True,
        ),
    ]
