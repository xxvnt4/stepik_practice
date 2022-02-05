from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area),
    path('rectangle/<width>/<height>', views.get_rectangle_area_error),
    path('square/<int:width>', views.get_square_area),
    path('square/<width>', views.get_square_area_error),
    path('circle/<int:radius>', views.get_circle_area),
    path('circle/<radius>', views.get_circle_area_error)
]
