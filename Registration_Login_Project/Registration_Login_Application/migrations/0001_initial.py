# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('location', multiselectfield.db.fields.MultiSelectField(max_length=200, choices=[('hyd', 'HYDERABAD'), ('bang', 'BANGALORE'), ('che', 'CHENNAI'), ('mum', 'MUMBAI')])),
                ('job', multiselectfield.db.fields.MultiSelectField(max_length=200, choices=[('HR', 'HR'), ('SOFTWARE', 'SOFTWARE'), ('MANAGER', 'MANAGER'), ('ADMIN', 'ADMIN')])),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=80)),
            ],
        ),
    ]
