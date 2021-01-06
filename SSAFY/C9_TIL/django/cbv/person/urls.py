from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('', views.PersonList.as_view(), name='list'),
    path('create/', views.PersonCreate.as_view(), name='create'),
]