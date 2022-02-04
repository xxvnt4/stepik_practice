from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Создаем словарь для того, чтобы избавиться от бесконечных elif
# С помощью него мы будем обращаться к нужному нам знаку зодиака
zodiac_dict = {
    'aries': 'Aries: March 21 - April 19',
    'taurus': 'Taurus: April 20 - May 20',
    'gemini': 'Gemini: May 21 - June 21'
}


def get_zodiac_info(request, zodiac_sign):
    description = zodiac_dict.get(
        zodiac_sign)  # Пытаемся получить значение по ключу в уже созданном словаре zodiac_dict
    if description:  # Если ключ есть в словаре, возвращается соответствующее значение
        return HttpResponse(description)
    else:  # Если нет ключа, возвращается соответствующее сообщение
        return HttpResponseNotFound(f'No information about {zodiac_sign}!')


# Вызов функции при конвертировании полученного значения в число
def get_zodiac_info_by_number(request, zodiac_sign: int):
    return HttpResponse(f'This is number {zodiac_sign}.')
