from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def get_zodiac_info(request, zodiac_sign):
    if zodiac_sign == 'aries':
        return HttpResponse('Aries: March 21 - April 19')
    elif zodiac_sign == 'taurus':
        return HttpResponse('Taurus: April 20 - May 20')
    elif zodiac_sign == 'gemini':
        return HttpResponse('Gemini: May 21 - June 21')
    else:
        return HttpResponseNotFound(f'No information about {zodiac_sign}!')
