from django.urls import path
from . import views

app_name = 'votes'

urlpatterns = [
    path('menu/', views.menu, name='menu'),
]