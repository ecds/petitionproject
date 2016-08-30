# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Author', models.CharField(max_length=255, null=True, verbose_name=b"Author's Name", blank=True)),
                ('Author_prefecture', models.CharField(max_length=255, null=True, blank=True)),
                ('Birth_year', models.CharField(max_length=255, null=True, blank=True)),
                ('Death_year', models.CharField(max_length=255, null=True, blank=True)),
                ('Details', models.TextField(null=True, blank=True)),
                ('Office', models.CharField(max_length=255, null=True, blank=True)),
                ('Other_names', models.CharField(max_length=255, null=True, blank=True)),
                ('Rank', models.CharField(max_length=255, null=True, blank=True)),
                ('Romanized_name', models.CharField(max_length=255, null=True, blank=True)),
                ('Sources', models.TextField(null=True, blank=True)),
                ('Status', models.TextField(null=True, blank=True)),
                ('urls', models.TextField(null=True, blank=True)),
                ('blue', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Authors',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
