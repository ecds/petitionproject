# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0010_remove_texts_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texts',
            name='Petition_number',
        ),
        migrations.AddField(
            model_name='texts',
            name='_Petition_number',
            field=models.CharField(max_length=255, null=True, db_column=b'Petition_number', blank=True),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Armstrong_checked',
            field=models.BooleanField(choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Date_unclear',
            field=models.BooleanField(choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='texts',
            name='Ravina_checked',
            field=models.BooleanField(choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
