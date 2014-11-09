# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, blank=True)),
            ],
            options={
                'ordering': ['province'],
                'verbose_name': 'Municipality',
                'verbose_name_plural': 'Municipalities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('code', models.CharField(max_length=2, verbose_name=b'Code')),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='municipality',
            name='province',
            field=models.ForeignKey(related_name='municipalities', to='geodz.Province'),
            preserve_default=True,
        ),
    ]
