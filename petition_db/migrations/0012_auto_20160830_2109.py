# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0011_auto_20160830_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='_Petition_number',
            field=models.IntegerField(null=True, db_column=b'Petition_number', blank=True),
        ),
    ]
