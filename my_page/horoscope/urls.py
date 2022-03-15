from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('<zodiac_value>/', views.get_zodiac_type_list, name='horoscope_value'),
    path('<int:month>/<int:day>/', views.determine_zodiac_sign),
    path('<str:month>/<str:day>/', views.determine_zodiac_sign_error)
]
