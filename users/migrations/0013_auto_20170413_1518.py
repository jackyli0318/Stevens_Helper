# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170403_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractive',
            name='expire_date',
            field=models.CharField(auto_created='2017-04-14', max_length=50, verbose_name='Expire date'),
        ),
    ]
