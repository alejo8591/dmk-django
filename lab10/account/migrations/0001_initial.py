# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user_profile_website', models.URLField(null=True, blank=True, help_text='Ingrese su sitio Web')),
                ('user_profile_picture', models.ImageField(null=True, blank=True, upload_to='profile_images')),
                ('user_profile_identification', models.CharField(unique=True, max_length=24, verbose_name='Identificacion', help_text='Ingrese su numero de Identificacion')),
                ('user_profile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
