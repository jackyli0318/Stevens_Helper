# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20170413_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='replyer',
        ),
        migrations.AddField(
            model_name='message',
            name='replier',
            field=models.CharField(default='', max_length=100, verbose_name='Replier'),
            preserve_default=False,
        ),
    ]
