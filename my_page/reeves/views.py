from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны'
    }
    return render(request, 'reeves/info.html', context=data)