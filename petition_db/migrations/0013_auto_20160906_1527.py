# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0012_auto_20160830_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Prefecture',
            field=models.IntegerField(blank=True, max_length=255, null=True, choices=[(1, b'\xe5\x90\x8d\xe5\x8f\xa4\xe5\xb1\x8b\xe7\x9c\x8c'), (2, b'\xe8\x86\xb3\xe6\x89\x80\xe7\x9c\x8c')]),
        ),
    ]
