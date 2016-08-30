# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0003_auto_20160830_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='texts',
            options={'verbose_name': 'Texts', 'verbose_name_plural': 'Texts'},
        ),
        migrations.AddField(
            model_name='texts',
            name='Authors',
            field=models.ManyToManyField(to='petition_db.Authors', blank=True),
        ),
    ]
