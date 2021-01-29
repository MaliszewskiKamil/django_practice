# Generated by Django 3.1.5 on 2021-01-29 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_name', models.CharField(default='Bob', max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fav_movie_char.movie')),
            ],
        ),
    ]
