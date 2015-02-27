# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launcher', '0005_auto_20150222_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesteduser',
            name='ip_address',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
    ]
