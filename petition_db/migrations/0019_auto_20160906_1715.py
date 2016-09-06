# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0018_auto_20160906_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Date_unclear',
            field=models.NullBooleanField(),
        ),
    ]
