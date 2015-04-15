# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150407_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='corporate_training',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='spec_injuryrec',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='spec_nutrition',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='spec_oly',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='spec_senior',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='spec_sporttrain',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='spec_weightmgmt',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='spec_youth',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='womens_only',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'No'), (2, b'Yes')]),
        ),
    ]
