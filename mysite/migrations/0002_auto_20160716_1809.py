# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField()),
                ('last_update_date', models.DateField()),
                ('staus', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='accounts',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 7, 16, 18, 9, 50, 686700, tzinfo=utc)),
        ),
    ]