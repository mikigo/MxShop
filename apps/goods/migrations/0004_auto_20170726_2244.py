# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 22:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goodscategorybrand_cagetory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodscategorybrand',
            old_name='cagetory',
            new_name='category',
        ),
    ]
