# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-19 09:03


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0011_auto_20170525_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalstockrecord',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalstockrecord',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='historicalstockrecord',
            name='product',
        ),
        migrations.DeleteModel(
            name='HistoricalStockRecord',
        ),
    ]