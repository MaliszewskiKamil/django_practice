# Generated by Django 3.1.5 on 2021-02-03 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('codedmind_blog', '0005_auto_20210203_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_published'),
        ),
    ]
