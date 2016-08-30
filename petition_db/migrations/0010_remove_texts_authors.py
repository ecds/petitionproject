# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0009_auto_20160830_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texts',
            name='Authors',
        ),
    ]
