# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0020_auto_20160906_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Petition_number',
            field=models.CharField(max_length=255, null=True, db_column=b'Petition_number', blank=True),
        ),
    ]
