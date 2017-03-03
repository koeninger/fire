# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 22:54
from __future__ import unicode_literals

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    Repository = apps.get_model('fb_github', 'Repository')
    for row in Repository.objects.all():
        row.uuid = uuid.uuid4()
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('fb_github', '0005_repository_uuid'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]