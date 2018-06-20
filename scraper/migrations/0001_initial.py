# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=1000, null=True, default='no title found')),
                ('slug', autoslug.fields.AutoSlugField(unique=True, null=True, editable=False, populate_from='title')),
                ('author', models.CharField(max_length=500, null=True, default='no author found')),
                ('date', models.CharField(max_length=100, null=True, default='no date found')),
                ('size', models.CharField(max_length=100, null=True, default='size not available')),
                ('download_link', models.CharField(max_length=1000, null=True, default='download link not available')),
                ('category', models.CharField(max_length=1000, null=True, default='Technology')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30, blank=True, null=True, default='Anonymous')),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField(max_length=2000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
                'ordering': ('-timestamp',),
            },
        ),
    ]
