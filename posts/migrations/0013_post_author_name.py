# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='admin', max_length=100, verbose_name='Author Name'),
            preserve_default=False,
        ),
    ]
