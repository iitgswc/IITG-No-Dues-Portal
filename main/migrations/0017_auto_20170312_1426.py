# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20170312_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.RemoveField(
            model_name='assistant_registrar',
            name='password',
        ),
        migrations.RemoveField(
            model_name='caretaker',
            name='password',
        ),
        migrations.RemoveField(
            model_name='cc',
            name='password',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='password',
        ),
        migrations.RemoveField(
            model_name='gymkhana',
            name='password',
        ),
        migrations.RemoveField(
            model_name='hod',
            name='password',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='password',
        ),
        migrations.RemoveField(
            model_name='library',
            name='password',
        ),
        migrations.RemoveField(
            model_name='onlinecc',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='submitthesis',
            name='password',
        ),
        migrations.RemoveField(
            model_name='warden',
            name='password',
        ),
    ]
