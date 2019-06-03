# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('liqd_product_users', '0004_use_url_field_for_homepage')]

    dependencies = [
        ('a4_candy_users', '0003_bio_text_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='homepage',
            field=models.URLField(blank=True, max_length=50, verbose_name='Homepage'),
        ),
    ]