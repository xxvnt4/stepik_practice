from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

todo_dict = {
    'monday': 'first',
    'tuesday': 'second',
    'wednesday': 'third',
    'thursday': 'fourth',
    'friday': 'fifth',
    'saturday': 'sixth',
    'sunday': 'seventh',
}


def get_day_number(request, day: int):
    if day > 0 and day < 8:
        return HttpResponse(f'Today is the {day} day of a week!')
    else:
        return HttpResponseNotFound(f'There is no the {day} day in a week!')


def get_todo_list(request, day):
    description = todo_dict.get(day)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'There is no such day as {day}!')
