# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170308_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud_lab_status',
            name='lab_remarks',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='stud_faculty_status',
            name='faculty_remarks',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
