# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='blue',
        ),
    ]
