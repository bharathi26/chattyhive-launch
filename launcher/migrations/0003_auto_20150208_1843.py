# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launcher', '0002_interesteduser_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesteduser',
            name='timestamp',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
