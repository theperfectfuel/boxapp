# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150406_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='crossfit_kids',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='drop_ins',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='kids_area',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='lifting_platforms',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='showers',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
    ]
