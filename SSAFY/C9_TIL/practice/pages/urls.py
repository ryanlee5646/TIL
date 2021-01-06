from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='list'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:page_id>/', views.detail, name='detail'),
    path('<int:page_id>/delete/', views.delete, name='delete'),
   
    
]