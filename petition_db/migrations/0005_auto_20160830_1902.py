# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0004_auto_20160830_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Day',
            field=models.IntegerField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Month',
            field=models.IntegerField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Number_in_arabic_numbers',
            field=models.IntegerField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Year',
            field=models.IntegerField(max_length=4, null=True, blank=True),
        ),
    ]
