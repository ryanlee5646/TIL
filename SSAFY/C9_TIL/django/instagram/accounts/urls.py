from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.password, name='password'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('<int:user_id>/follow/', views.follow, name="follow"), # 누구를 follow할건지에 대한 user_id(유저정보)
    
]