# Generated by Django 4.0.4 on 2022-05-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_director_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='director',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
