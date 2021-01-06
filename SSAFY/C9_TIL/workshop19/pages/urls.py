from django.urls import path
from . import views
# url파일을 따로 관리하기 위해 새로 생성하고 이 앱폴더 안에있는
# views파일을 import함
urlpatterns = [
    path('', views.index), #index 주소는 /student뒤에 아무것도 없이 입력
    path('new/', views.new),
    path('create/', views.create),
    path('<int:student_id>/', views.detail),
    path('<int:student_id>/delete/', views.delete),
    path('<int:student_id>/edit/', views.edit),
    # path('<int:student_id>/update/', views.update),
]