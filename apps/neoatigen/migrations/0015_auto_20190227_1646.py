# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-27 16:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoatigen', '0014_auto_20190222_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='finish_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='finish_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='peptide',
            name='finish_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
    ]
