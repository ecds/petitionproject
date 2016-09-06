# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0014_auto_20160906_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Prefectures', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='texts',
            name='Prefecture',
            field=models.ForeignKey(blank=True, to='petition_db.Prefectures', null=True),
        ),
    ]
