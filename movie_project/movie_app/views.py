from django.shortcuts import render, get_object_or_404
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
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