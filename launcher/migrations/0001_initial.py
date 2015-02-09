# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterestedUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('email', models.EmailField(max_length=75)),
                ('subject', models.CharField(max_length=128, null=True)),
                ('content', models.TextField()),
                ('via', models.CharField(max_length=24)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
