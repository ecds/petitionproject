# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0019_auto_20160906_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='texts',
            old_name='_Petition_number',
            new_name='Petition_number',
        ),
    ]
