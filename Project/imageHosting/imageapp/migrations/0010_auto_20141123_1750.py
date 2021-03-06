# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import imageapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0009_auto_20141117_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'C:\\Project\\imageHosting\\image_space\\photos'), upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='profile_pic',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'C:\\Project\\imageHosting\\image_space\\photos\\profile_pics'), upload_to=imageapp.models.get_profile_pic_name),
            preserve_default=True,
        ),
    ]
