# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_student_gymkhana_approval'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='onlinecc_approval',
            new_name='online_cc_approval',
        ),
    ]
