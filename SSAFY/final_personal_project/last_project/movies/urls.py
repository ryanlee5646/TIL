from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('', views.movie_list, name="list"),
    
    path('<int:movie_id>/',views.movie_detail, name='detail'),
    path("<int:movie_id>/like/", views.like, name="like"),
    path('search/',views.search, name="search"),
    path('<int:movie_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:movie_id>/comments/<int:comment_score_id>/delete',views.comments_delete,name='comments_delete'),
    path('top/',views.top, name="top"),
    path('selfsearch/',views.selfsearch, name="selfsearch"),
    path('selftop/', views.selftop, name="selftop"),
    # path('<int:post_id>/movie_update/', views.update, name='update'),
    # path('<int:post_id>/movie_delete/', views.delete, name='delete'),
    
]