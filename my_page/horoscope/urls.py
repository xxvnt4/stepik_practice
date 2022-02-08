from django.urls import path
from . import views

# Конвертеры роутов
# Здесь важен порядок
# Сначала пытаемся конвертировать роут в целое число, потом - в строку
# Доступные типы для конвертации в документации Django
urlpatterns = [
    path('', views.index),
    # Добавляем еще один роут для того, чтобы обработать URL horoscope/ без названия знака зодиака
    # views.index - функция, которая будет обрабатывать запрос
    path('<int:zodiac_sign>/', views.get_zodiac_info_by_number),
    path('<str:zodiac_sign>/', views.get_zodiac_info, name='horoscope-name')
]
