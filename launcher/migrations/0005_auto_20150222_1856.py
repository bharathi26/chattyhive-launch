# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launcher', '0004_auto_20150208_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesteduser',
            name='content',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interesteduser',
            name='email',
            field=models.EmailField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interesteduser',
            name='name',
            field=models.CharField(null=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interesteduser',
            name='subject',
            field=models.CharField(null=True, max_length=256),
            preserve_default=True,
        ),
    ]
