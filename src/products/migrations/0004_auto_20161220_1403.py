# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to_featured)),
                ('title', models.CharField(max_length=120, null=True, blank=True)),
                ('text', models.CharField(max_length=220, null=True, blank=True)),
                ('text_right', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=products.models.image_upload_to),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(related_name='default_category', blank=True, to='products.Category', null=True),
        ),
    ]
