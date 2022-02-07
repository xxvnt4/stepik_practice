from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area),
    path('rectangle/<width>/<height>', views.get_rectangle_area_error),
    path('get_rectangle_area/<int:width>/<int:height>', views.redirect_rectangle_area),
    path('get_rectangle_area/<width>/<height>', views.get_rectangle_area_error),
    path('square/<int:width>', views.get_square_area),
    path('square/<width>', views.get_square_area_error),
    path('get_square_area/<int:width>', views.redirect_square_area),
    path('get_square_area/<width>', views.get_square_area_error),
    path('circle/<int:radius>', views.get_circle_area),
    path('circle/<radius>', views.get_circle_area_error),
    path('get_circle_area/<int:radius>', views.redirect_circle_area),
    path('get_circle_area/<radius>', views.get_circle_area_error)
]
