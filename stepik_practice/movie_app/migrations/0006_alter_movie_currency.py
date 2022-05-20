# Generated by Django 4.0.2 on 2022-05-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollars'), ('RUB', 'Rubles')], default='RUB', max_length=3),
        ),
    ]
