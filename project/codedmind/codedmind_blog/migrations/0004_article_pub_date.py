# Generated by Django 3.1.5 on 2021-02-03 11:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codedmind_blog', '0003_auto_20210203_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 11, 23, 3, 897927, tzinfo=utc), verbose_name='date_published'),
            preserve_default=False,
        ),
    ]
