# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0016_auto_20160906_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Armstrong_checked',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Date_unclear',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Ravina_checked',
            field=models.NullBooleanField(),
        ),
    ]
