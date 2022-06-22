from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.age}'