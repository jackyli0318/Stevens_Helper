# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170302_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractive',
            name='expire_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2017, 3, 3, 16, 43, 26, 283159), verbose_name='Expire date'),
        ),
    ]
