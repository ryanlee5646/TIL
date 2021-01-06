### #07 Project를 통한 장고 정리

1. **project를 담을 폴더 생성(project_07)**
2.  **Django 환경설정**

```bash
$ cd project_07(프로젝트 폴더로 이동)
$ pyenv virtualenv 3.6.7 pro07(환경명)-venv
$ pyenv local pro07-venv
-> (pro07-venv) ryanlee5646:/workspce/project_07
```

3. **Django 설치**

```bash
$ pip install django==2.1.8 (장고 신버전 2.2가 나왔는데 c9이 서비스를 접는다고 해서 구버전으로 설치)
$ django-admin startproject project_07 . (프로젝트명 지정 후 현재 폴더란 의미의 .을 찍어줘야함)
$ python manage.py runserver $IP:$PORT (서버를 실행하는 명령어 입력) 
```

4. **Django Setting**

```python
# settings.py(서버 등록)
ALLOWED_HOSTS = ['playground-ryanlee5646.c9users.io'] 

# App 생성(bash에서)
$ python(or ./) manage.py startapp movies(앱이름) #app이름은 복수로 지정

# settings.py(App등록)
INSTALLED_APPS = [
    'movies.apps.moviesConfig',(습관적으로 ,찍어주는게 좋음, 그리고 앱이름만 movies로 해도 됌)
]
```

5. **Urls Setiing**

```python
# urls.py(프로젝트(project_07) 폴더안에)
# url을 app 폴더 안에서 따로 관리해주기 위해 경로를 설정해줌
from django.contrib import admin
form django.urls import path, 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')) 
    # include함수로 movies 폴더에 있는 urls 호출 
]

# urls.py(movies폴더(App폴더 안에 있는)를 생성)
from django.urls import path
from . import views 

app_name = 'movies' #urls.py가 어디 소속인지 명시

urlpatterns = [
    
]
```

6. **데이터베이스 테이블 설정(models.py)**

```python
# models.py
form django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100) # 장르명
	# CharField는 max_length를 정해줘야함
class Movie(models.Model):
    title = models.CharField(max_length=100) # 영화명
    audience = models.IntegerField() # 누적 관객수
    poster_url = models.TextField() # 포스터 이미지
    description = models.TextField() # 영화소개
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) 
    # 장르의 Primary키값(_id붙일 필요없음)
    
class Score(models.Model):
    content = models.CharField(max_length=100) # 한줄평 평가내용
    score = models.IntegerField() # 평점
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 장르의 Primary키값(_id붙일 필요없음)
    
#데이터베이스에 적용하기 위해 명령어 입력
$./manage.py makemigrations (#데이터 베이스를 옮기기 위한 설계도, 만약 models.py 내용이 수정되었다면 다시 명령어를 입력해야함)
$./manage.py migrate (# models.py 설계도를 바탕으로 데이터베이스 생성)
*주어진 csv파일을 프로젝트 폴더 가장 바깥에 올리기
# csv에 있는 데이터를 불러오기 위해 sqlite실행
$ sqlite3 db.sqlite3
    >> .mode csv
    >> .import genre.csv movies_genre
    >> .import movie.csv movies_movie
    # INSERT failed: UNIQUE constraint failed: movies_movie.id
    # 이런 메세지가 떠도 당황 nono 데이터 잘 들어 간거임

    

```

7. **관리자(admin) 페이지 생성**

```python
# admin.py
from django.contrib import admin
from .models import Movie,Genre,Score 
# models.py에 있는 각 테이블(클래스)들을 불러온다

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Score)

# 관리자 페이지를 만든 후 데이터베이스를 관리 할 수 있는 관리자 계정 생성
$ ./manage.py createsuperuser
```

8. **페이지 만들기(base.html)**

**모든 템플릿에 적용할 base.html을 프로젝트폴더안에 templates 폴더를 생성 후 생성**

```python
# settings.py에서 base.html 경로 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'project_07','templates')],
```

```html
<!-- base.html -->
!을 눌러 자동 완성 후 적용할 Component를 body아래 작성 후
body가 끝나기 전에 다음 코드를 입력

{% block container %}
{% endblock %}
```

9. **영화목록 페이지 만들기(list.html)**

```python
# view.py
def list(request):
    movies = Movie.objects.all() # movies 변수에 Movie 테이블에 있는 모든 데이터를 저장
    return render(request, 'list.html',{'movies':movies})
```

```python
# urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.list, name='list'), #기본 /movies로 설정, 그리고 링크 name 지정
]
```

```html
<!-- list.html -->
{% extends 'base.html' %} <!-- base.html을 불러오고 -->

{% block container %} <!-- 시작지점과-->

<h1> 영화 목록 </h1>
{% for movie in movies %} <!-- view.py에서 변수로 저장된 모든 데이터를 진자템플릿을 이용한 for문으로 정보를 출력하도록함 -->
<img src="{{ movie.poster_url }}"> <!-- 영화 포스터 -->

<a href="{% url 'movies:detail' movie.id %}">{{ movie.title }}</a>
<!-- a태그를 이용하여 영화 제목을 클릭하면 영화상세페이지(detail.html)로 넘어가게 함 -->
<br>
{% endfor%} <!-- for문이 끝나면 닫아줘야함 -->
{% endblock %} <!--끝 지점을 감싸준다 -->
```

10. **영화 상세페이지 만들기 (detail.html)**

```python
# views.py
from django.shortcuts import render,redirect, get_object_or_404
#get_object_or_404를 호출해 줘야한다.
from .models import Movie
def detail(request, movie_id):
    #movie = Movie.objects.get(pk=movie_id) 
    # 영화 키값별로 get방식으로 받은 정보를 movie 변수에 저장()
    # 이 방식은 페이지가 없다면 500error(서버에러)가 발생한다.
    movie = get_object_or_404(Movie, id=movie_id)
    # 이 방식은 404error(페이지에러)가 발생하는데 사용자 기준으로 봤을 때
    # 이 방식을 쓰는 것을 선호
    return render(request, 'detail.html', {'movie':movie})
```

```python
# urls.py
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:movie_id>/detail/', views.detail, name='detail'),
    # 동적할당되는 키값 코드를 넣어줌
]
```

```html
<!-- detail.html -->
{% extends 'base.html' %}

{% block container %}
<h2>{{ movie.title }}</h2>
<img src="{{ movie.poster_url }}"> <!-- 이미지 tag를 통해 이미지 출력 -->
<p>장르: {{ movie.genre.name }}</p> <!-- Movie테이블 안에 있는 장르(genre) 변수에는 Genre테이블 안에서 받아온 외래키값(ForeignKey)이 저장되있다. 그 키값을 바탕으로 장르 출력 -->
<p>누적관객수: {{ movie.audience }}</p>
<p>요약: {{ movie.description }}</p>
<p>포스터url: {{movie.poster_url}}</p>

{% endblock %}
```

11.  **영화 상세페이지 아래 '목록', '수정', '삭제' 링크 만들기**

```html
<!-- 목록 -->
<!-- detail.html -->
<a href="{% url 'movies:list' %}">목록</a>
<!-- a태그를 이용해 list 링크로 보냄 -->
```

```python
# 삭제
# views.py
def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('moveis:list') # 삭제하고 목록페이지로 redirect
# urls.py
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/delete/', views.delete, name='delete'), # 링크에 키값을 할당
]
# detail.html
<a href="{% url 'movies:delete' movie.id %}">삭제</a> # 삭제버튼을 누르면 delete
```

```python
# 수정
# views.py
def update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST': # 수정버튼을 누르고 수정한 후 Submmit 누르면 Post방식
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:detail', movie_id)
        else: # 수정 버튼을 누르기만하면 get방식
            movie_form = MovieForm(instance=movie)
        return render(request,'update.html',{'movie_form':movie_form})
# urls.py
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/update/', views.update, name='update'),
]
# detail.html
<a href="{% url 'movies:update' movie.id %}">수정</a>

# forms.py
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie # models.py Movie테이블을 가져옴
        fields = ['title', 'audience', 'poster_url', 'description',] # 나타낼 필드를 선택
        
# update.html
{% extends 'base.html' %}

{% block container %}

<form method='POST'>
    {% csrf_token %} 
    {{ movie_form.as_p }} <!-- movie_form안에 항목을 p태크로 감싸서 한줄에 한 항목이 오도록함. -->
    <input type="submit" value="Submit"/>
</form>

{% endblock %}
```

12. **평점 생성, 삭제하기**

```python

# forms.py
from django import forms
from .models import Score, Movie

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score # Score 테이블을 가져옴
        fields = ['content', 'score', ] # 표시할 필드(내용, 평점)
    
# views.py
from .models import Movie, Genre, Score # Score 테이블을 불러옴
from .forms import ScoreForm, MovieForm # ScoreForm을 불러옴
def score_new(request, movie_id):
    score_form = ScoreForm(request.POST) # 페이지에서 Submit한 상태
    if score_form.is_valid(): # 유효한지 판단.(예를들어 FieldType에 맞게 입력됐는지, 비어있지는 않은지)
        score = score_form.save(commit=False) # 실제 데이터베이스에 반영하지 않고 일단 Score객체만 가져옴
        # score.movie = get_object_or_404(Movie, id=movie_id)
        score.movie_id = movie_id # 이렇게 해도 동작은 함(바로 저장하지 않고 이렇게 하는 이유는
        # Submit한 페이지에는 영화의 키값을 입력하는 정보가 없기 때문에.)
        score.save() # 실제로 데이터베이스에 저장
        return redirect('movies:detail', movie_id)
    
 def score_delete(request, movie_id, score_id): #urls.py movie키값과 score 키값을 넘겨줌
    score = get_object_or_404(Score, id=score_id)
    score.delete()
    return redirect('movies:detail', movie_id)
    
#url.py
path('', views.list, name='list'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/update/', views.update, name='update'),
    path('<int:movie_id>/scores/new/', views.score_new, name='score_new'),

# detail.html
{% for score in movie.score_set.all %} #view.py detail에 있는 movie변수
    <p>{{ score.content}} {{ score.score }}
    <a href="{% url 'movies:score_delete' movie.id score.id %}">
        <button type='button' class='btn btn-danger btn-sm'> 삭제 </button>
    </a>
    </p>
{% endfor %}
<form action ="{% url 'movies:score_new' movie.id %}" method='POST'>
    {% csrf_token %}
    {{ score_form }}
    <input type="submit" value="Submit"/>
</form>
```



12. 



