# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesteduser',
            name='timestamp',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
