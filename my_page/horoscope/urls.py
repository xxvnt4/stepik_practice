from django.urls import path
from . import views

# Конвертеры роутов
# Здесь важен порядок
# Сначала пытаемся конвертировать роут в целое число, потом - в строку
# Доступные типы для конвертации в документации Django
urlpatterns = [
    path('<int:zodiac_sign>/', views.get_zodiac_info_by_number),
    path('<str:zodiac_sign>/', views.get_zodiac_info),
]
