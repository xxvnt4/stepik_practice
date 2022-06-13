# Generated by Django 4.0.4 on 2022-06-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_actor_movie_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
