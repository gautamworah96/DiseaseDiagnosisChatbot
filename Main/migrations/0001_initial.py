# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-12 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='symptoms',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('d_id', models.BigIntegerField()),
                ('symptom', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'symptoms',
            },
        ),
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('cause', models.TextField()),
                ('treatment', models.TextField()),
            ],
        ),
    ]