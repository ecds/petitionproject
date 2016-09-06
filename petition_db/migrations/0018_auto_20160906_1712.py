# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0017_auto_20160906_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Date_unclear',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
