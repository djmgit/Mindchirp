# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0004_auto_20160325_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='no image available for this post', upload_to='images/%Y/%m/%d'),
        ),
    ]