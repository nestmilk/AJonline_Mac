# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-24 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoatigen', '0011_auto_20190124_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='express_company',
            field=models.CharField(choices=[('SF', '\u987a\u4e30\u5feb\u9012'), ('YT', '\u5706\u901a\u5feb\u9012'), ('ST', '\u7533\u901a\u5feb\u9012'), ('YD', '\u97f5\u8fbe\u5feb\u9012'), ('ZS', '\u81ea\u9001')], default='SF', max_length=10, verbose_name='\u5feb\u9012\u516c\u53f8'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='express_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5feb\u9012\u5355\u53f7'),
        ),
    ]
