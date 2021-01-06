from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('update/', views.profile_update, name='profile_update'),
    path('delete/', views.delete, name='delete'),
    path('password/',views.password, name='password'),
    path('check/', views.check, name='check'),
    path('profile/update/', views.profile_update, name='profile_update'),
]