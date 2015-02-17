# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150209_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_slug',
            field=models.SlugField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
