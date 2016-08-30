# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition_db', '0002_remove_authors_blue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sort_key', models.CharField(max_length=255, null=True, blank=True)),
                ('Title', models.CharField(max_length=255, null=True, blank=True)),
                ('Clean_text', models.TextField(null=True, blank=True)),
                ('Year', models.CharField(max_length=255, null=True, blank=True)),
                ('Month', models.CharField(max_length=255, null=True, blank=True)),
                ('Day', models.CharField(max_length=255, null=True, blank=True)),
                ('Number_in_arabic_numbers', models.CharField(max_length=255, null=True, blank=True)),
                ('Petition_number', models.CharField(max_length=255, null=True, blank=True)),
                ('Original_or_copy', models.CharField(max_length=255, null=True, blank=True)),
                ('Date_in_Japanese', models.CharField(max_length=255, null=True, blank=True)),
                ('Paper_type', models.CharField(max_length=255, null=True, blank=True)),
                ('Prefecture', models.CharField(blank=True, max_length=255, null=True, choices=[(b'1', b'1'), (b'2', b'2')])),
                ('Detailed_location', models.CharField(max_length=255, null=True, blank=True)),
                ('Temp_residence', models.CharField(blank=True, max_length=255, null=True, choices=[(b'1', b'1'), (b'2', b'2')])),
                ('Author_position', models.CharField(max_length=255, null=True, blank=True)),
                ('Author', models.CharField(max_length=255, null=True, blank=True)),
                ('Addressee', models.CharField(max_length=255, null=True, blank=True)),
                ('Archive', models.CharField(max_length=255, null=True, blank=True)),
                ('Date_unclear', models.BooleanField()),
                ('Title_source', models.CharField(blank=True, max_length=255, null=True, choices=[(b'From text', b'From text'), (b'Assigned by editors', b'Assigned by editors'), (b'Assigned by institution', b'Assigned by institution')])),
                ('Ravina_checked', models.BooleanField()),
                ('Armstrong_checked', models.BooleanField()),
                ('Corrections', models.TextField(null=True, blank=True)),
                ('Last_action', models.CharField(max_length=255, null=True, blank=True)),
                ('Number_finder', models.CharField(max_length=255, null=True, blank=True)),
                ('Genro', models.CharField(max_length=255, null=True, blank=True)),
                ('Glitch', models.CharField(max_length=255, null=True, blank=True)),
                ('Full_text_with_CR', models.TextField(null=True, blank=True)),
                ('NEWLINE', models.CharField(max_length=255, null=True, blank=True)),
                ('Processing', models.TextField(null=True, blank=True)),
                ('Count', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='authors',
            name='Petitions',
            field=models.ManyToManyField(to='petition_db.Texts', blank=True),
        ),
    ]
