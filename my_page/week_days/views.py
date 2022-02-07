from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    days = list(todo_dict)
    if day <= 0 or day > 7:
        return HttpResponseNotFound(f'Неправильный порядковый номер дня недели!')
    return HttpResponseRedirect(f'/week_days/{days[day - 1]}')


def get_todo_list(request, day):
    description = todo_dict.get(day)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'There is no such day as {day}!')
