# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 10:51
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tablets', '0002_add_mptt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='template',
            options={'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
        migrations.AlterField(
            model_name='template',
            name='default_context',
            field=jsonfield.fields.JSONField(blank=True, default=dict, help_text='Does not work so well for Jinja2 templates, which throw exceptions for missing values. This can make things tough if your template relies on functions.', verbose_name='Default Context'),
        ),
    ]