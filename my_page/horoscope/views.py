from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    zodiacs = list(zodiac_dict)  # Присваиваем переменной список из ключей словаря
    if zodiac_sign > len(zodiacs):  # Если введенное пользователем число будет больше
        # длины нашего списка, вернется соответствующее сообщение
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {zodiac_sign}!')
    name_zodiac = zodiacs[zodiac_sign - 1]  # Если все хорошо, то мы преобразуем полученное число в знак зодиака и
    # по полученному URL обратимся к нужной нам функции
    # ---
    # Чтобы не переписывать во всех местах horoscope, если в my_page.urls мы изменим это название, используем
    # функцию reverse из модуля django.urls.
    # В аргументах укажем значение переменной name, которое мы передали функции path в urlpatterns нашего приложения.
    # А в args списком запишем переменную name_zodiac.
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
