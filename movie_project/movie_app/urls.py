from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    # Создадим новый роут для того, чтобы можно было обращаться к информации о фильме по slug в адресной строке.
]
