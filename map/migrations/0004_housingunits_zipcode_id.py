# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20151005_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='housingunits',
            name='zipcode_id',
            field=models.IntegerField(default=0),
        ),
    ]
