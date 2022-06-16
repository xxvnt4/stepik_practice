from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.index, name='form_index'),
]