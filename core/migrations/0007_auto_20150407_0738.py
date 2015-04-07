# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150406_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=models.TextField(null=True, blank=True),
        ),
    ]
