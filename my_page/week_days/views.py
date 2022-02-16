from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    redirect_url = reverse('week_days_name', args=[days[day-1]])
    return HttpResponseRedirect(redirect_url)


def get_todo_list(request, day):
    return render(request, 'week_days/greeting.html')

def index(request):
    days = list(todo_dict)
    li_elements = ''
    for day in days:
        redirect_path = reverse('week_days_name', args=[day])
        li_elements += f'<li><a href="{redirect_path}">{day.title()}</a></li>'
    response = f'''
    <ol>
        {li_elements}
    </ol>
    '''
    return HttpResponse(response)