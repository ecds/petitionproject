# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0013_auto_20160906_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='Prefecture',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[('\u540d\u53e4\u5c4b\u770c', b'\xe5\x90\x8d\xe5\x8f\xa4\xe5\xb1\x8b\xe7\x9c\x8c'), ('\u540d\u53e4\u5c4b\u770c', b'\xe8\x86\xb3\xe6\x89\x80\xe7\x9c\x8c')]),
        ),
    ]
