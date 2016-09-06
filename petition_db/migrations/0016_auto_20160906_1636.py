# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0015_auto_20160906_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prefectures',
            options={'verbose_name': 'Prefectures', 'verbose_name_plural': 'Prefectures'},
        ),
        migrations.AlterField(
            model_name='texts',
            name='Armstrong_checked',
            field=models.NullBooleanField(choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Date_unclear',
            field=models.NullBooleanField(choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Ravina_checked',
            field=models.NullBooleanField(choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
