from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.index, name='form_index'),
    path('form/output/', views.form_output, name='form_output'),
]