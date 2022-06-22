from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('directors/', views.show_directors_list, name='directors_list'),
    path('director/<slug:slug_director>', views.show_one_director, name='director_detail'),
]
