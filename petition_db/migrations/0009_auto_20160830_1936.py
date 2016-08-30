# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0008_auto_20160830_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Last_action',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
