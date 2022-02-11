from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index),
    path('<yyyy:zodiac_value>/', views.get_yyyy_converters),
    path('<my_date:zodiac_value>/', views.get_my_date_converters),
    path('<int:zodiac_value>/', views.get_zodiac_info_by_number),
    path('<my_float:zodiac_value>/', views.get_my_float_converters),
    path('<zodiac_value>/', views.get_zodiac_type_list, name='zodiac_type_name'),
    path('<zodiac_value>/', views.get_zodiac_info, name='horoscope_name'),
    path('<int:month>/<int:day>/', views.determine_zodiac_sign),
    path('<str:month>/<str:day>/', views.determine_zodiac_sign_error)
]
