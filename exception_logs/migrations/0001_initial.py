# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-08 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralLog',
            fields=[
                ('dblogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exception_logs.DBLogEntry')),
            ],
            bases=('exception_logs.dblogentry',),
        ),
        migrations.CreateModel(
            name='SpeicalLog',
            fields=[
                ('dblogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exception_logs.DBLogEntry')),
            ],
            bases=('exception_logs.dblogentry',),
        ),
    ]
