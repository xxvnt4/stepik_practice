from django.shortcuts import render

def index(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': "Bob's BBQ & Grill",
        'count_needle': 1790
    }
    return render(request, 'guinness/guinnessworldrecords.html', context=context)
