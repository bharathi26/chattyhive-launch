# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launcher', '0003_auto_20150208_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesteduser',
            name='timestamp',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
