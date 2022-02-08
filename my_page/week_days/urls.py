from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:day>/', views.get_day_number),
    path('<str:day>/', views.get_todo_list, name='week_days_name'),
]
