# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_auto_20150422_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(null=True, verbose_name=b'Age', blank=True)),
                ('gender', models.IntegerField(blank=True, null=True, verbose_name=b'Gender', choices=[(1, b'Male'), (2, b'Female'), (3, b'Other')])),
                ('profile_image', models.ImageField(upload_to=core.models.upload_to_profile, null=True, verbose_name=b'Profile Image', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
