from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:zodiac_value>/', views.get_zodiac_info_by_number),
    path('<zodiac_value>/', views.get_zodiac_type_list, name='zodiac_type_name'),
    path('<zodiac_value>/', views.get_zodiac_info, name='horoscope_name'),
    path('<int:month>/<int:day>/', views.determine_zodiac_sign),
    path('<str:month>/<str:day>/', views.determine_zodiac_sign_error)
]
