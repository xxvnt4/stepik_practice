from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Actor(models.Model):
    # Создадим новую модель со связью Многие ко многим.
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    # Опишем необходимые переменные для поля gender.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        # Опишем поведения вывода в зависимости от пола актера или актрисы.
        if self.gender == self.MALE:
            return f'Actor {self.first_name} {self.last_name}'
        else:
            return f'Actresse {self.first_name} {self.last_name}'

class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000,
                                 validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)
    # Свяжем модель Actor с полем actors связью Многие ко многим.

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.rating}%'

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])
