# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 03:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20161112_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud_faculty_status',
            old_name='approved',
            new_name='faculty_approval',
        ),
        migrations.RenameField(
            model_name='stud_lab_status',
            old_name='approved',
            new_name='lab_approval',
        ),
    ]
