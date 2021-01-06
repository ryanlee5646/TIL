from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('new/', views.create, name='create'),
    path('<int:article_id>', views.detail, name='detail'),
    path('<int:article_id>/edit/', views.update, name='update'),
]