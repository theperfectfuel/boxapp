# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150415_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Address', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=300, null=True, verbose_name=b'City', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='corporate_training',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Corporate Training', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='crossfit_kids',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'CrossFit Kids', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Description of Your Gym', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='drop_ins',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Drop Ins', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='hours',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Hours', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='image_file',
            field=models.ImageField(upload_to=core.models.upload_to_location, null=True, verbose_name=b'Image', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='kids_area',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Kids Area', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='lifting_platforms',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Lifting Platforms', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='showers',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Showers', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='spec_injuryrec',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Injury Recovery', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='spec_nutrition',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Nutrition', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='spec_oly',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Olympic Style Weightlifting', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='spec_senior',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Senior Training', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='spec_sporttrain',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Sport Specific Training', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='spec_weightmgmt',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Weight Management', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='spec_youth',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Youth Training', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=300, null=True, verbose_name=b'State', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=300, verbose_name=b'Name of Your Gym'),
        ),
        migrations.AlterField(
            model_name='location',
            name='womens_only',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Womens Only Classes', choices=[(1, b'No'), (2, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='zipcode',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Zip Code', blank=True),
        ),
    ]
