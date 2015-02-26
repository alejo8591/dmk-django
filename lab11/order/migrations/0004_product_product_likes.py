# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_customer_customer_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_likes',
            field=models.IntegerField(blank=True, null=True, default=0),
            preserve_default=True,
        ),
    ]
