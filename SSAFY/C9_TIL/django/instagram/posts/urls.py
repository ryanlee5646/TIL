from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('explore/', views.explore, name='explore'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/create/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/comments/create/', views.comment_create, name ='comment_create'),
    path('<int:post_id>/comments/delete/<int:comment_id>/delete', views.comment_delete, name='comment_delete'), # 어떤 포스트에 어떤 댓글을 삭제할 건지에 대한 id값 모두 적용
    path('<int:post_id>/like/', views.like, name='like'),
]
