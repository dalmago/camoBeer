# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerCatalog', '0002_remove_beer_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='beer_type',
            field=models.IntegerField(choices=[(0, 'Lata'), (1, 'Latao'), (2, 'Garrafa'), (3, 'Litro')], default=0),
            preserve_default=False,
        ),
    ]
