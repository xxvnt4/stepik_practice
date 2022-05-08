from django.db.models import F, Max, Min, Avg, Value
# Из этого модуля импортируем три необходимые агрегирующие функции. Также есть Sum, Count.
from django.shortcuts import render, get_object_or_404

from .models import Movie


def show_all_movie(request):
    ### movies = Movie.objects.order_by(F('year').desc(nulls_last=True))
    # В данном случае, для сортировки Movie.objects используем метод order_by(), куда аргументом в виде строки
    # передаем название колонки, по которой будем сортировать.
    # Например, Movie.objects.order_by('year'), Movie.objects.order_by('rating'), Movie.objects.order_by('year', 'id').
    # В обратном порядке -- Movie.objects.order_by('-year'), Movie.objects.order_by('-rating').
    # Также, есть объект F, который импортируется из модуля django.db.models (см. выше в импортах). С помощью него тоже
    # можно выполнить сортировку, а также выбрать, где расположить элементы со значением NULL - выше или ниже (см. выше).
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget') + 100
    )
    # Метод .annotate() позволяет добавлять дополнительные вычисляемые поля к нашей модели. Они не сохраняются с базе
    # данных. Аргументами к этому методу идет любое количество новых полей типа <название>=Value(<значение>). Функция
    # Value импортируется из модуля моделей базы данных - см. выше в импортах.
    # Чтобы, например, создать вычисляемое поле с результатом сложения уже существующих полей, необходимо обратиться
    # к объекту F (импортируется оттуда же, откуда и Value). Аргументом к этому объекту идет название поля строкой.
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    # Используем метод aggregate(), куда аргументами передаем агрегирующие функции, которые хотим использовать.
    # Одним аргументом к последним передаем строкой название колонки, с которой хотим поработать.
    # Присвоим получившиеся значения переменной agg. Они, кстати, представляют собой словарь, ключи которого имеют вид
    # budget__avg, rating__max, rating__min. В дальнейшем, в шаблонах, будем к ним обращаться. Само собой, эту переменную
    # передадим в словарь context - см. ниже.
    context = {
        'movies': movies,
        'agg': agg
    }
    return render(request, 'movie_app/all_movies.html', context=context)


def show_one_movie(request, slug_movie:str):
    # Добавим еще одну функцию, которая будет отображать информацию об одном фильме. Эта функция аргументом принимает
    # переменную slug_movie.
    movie = get_object_or_404(Movie, slug=slug_movie)
    # Данной функцией мы получаем объект, а в случае отсутствия объекта с таким slug возвращается ошибка 404.
    context = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=context)
    # Выводим шаблон, передав необходимые нам переменные.