# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-25 19:20


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_siteconfiguration_journals_api_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessclient',
            name='enterprise_customer_uuid',
            field=models.UUIDField(blank=True, help_text='UUID for an EnterpriseCustomer from the Enterprise Service.', null=True, verbose_name='EnterpriseCustomer UUID'),
        ),
    ]
