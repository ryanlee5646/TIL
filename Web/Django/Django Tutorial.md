Django Tutorial



1. 장고 설치 및 설정

2. 함수 render는 특정한 페이지를 보여주는 response역할 만 함

   함수 redirect는 다시 돌려보내주는 역할을 함

```python
# views.py

def hello(request): #request는 정해진게 아니라 하나의 임의의 변수임
    #request 안에는 어떠한 사람이 이 주소를 치고 들어왔을때 정보가 다 들어 있음.
    return render(request, 'hello.html', {}) #첫번째 인자에는 요청, 두번째 인자에는 페이지
#
```

```python
# urls.py
from django.contrib import admin
from django.urls import path
from movies import views #view.py에 있는 뷰를 가지고오기 위해 위치를 import해야함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello), 
    # 모든 요청을 views.hello 함수로 다 던져줌
    # path라는 함수에 첫번째 인자로 문자열, 두번째 인자로 함수자체를 넘겨줌
  # views.py 에서 함수인자값으로 request를 정해준 이유가 path에서 들어온 정보를 담아줄 변수를 지정해줘야 하기때문에 정해줌

	path('hi/<str:apple>/', views.hi), #'<>'는 동적으로 들어가는 주소
    # apple이라는 변수에 들어오는 str을 저장
]
# views.py
def hi(request, apple): #두번째 인자값에 apple이라는 변수가 그대로 와야함.
    print(apple)
    return render(request, 'hi.html', {})

```



## CRUD

### URL 관리

```python
# project폴더 안에 urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')), # movies App폴더 안에 urls를 가져옴
    # movies/ 다음에 include한 주소명을 포함시켜서 함수로 넘겨줌
]

# app 폴더 안에 urls.py
from django.urls import path
from . import views # 함수를 호추랳야함

App_name = ['movies'] # 앱이름을 명시해 줘야함

urlpatterns = [
    path('create/', views.create) # project폴더안에 movies/뒤에 둘어감
]
```



### CREATE(생성)

```python
# models.py
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
# model(테이블) 생성 후 makemigrations 와 migrate를 해줌
```

```python
# views.py
from django.shortcuts import render

def create(request):
    return render(request, 'movies/create.html', {'movie_form': movie_form})
# urls.py
app_name = 'movies'
urlpatterns = [
    path('create/', views.create)
]

# forms.py
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm): # import해온 forms에서 ModelForm을 가져옴
    # ModelForm에게 
    class Meta:
        model = Movie
        fields = ['title'] # 모델에 있는 모든 정보를 써도 좋지만 부분적으로만 사용가능
        # 모든 field를 보여주고 싶을때는
        fields = '__all__'
        
 # ModelForm클래스를 상속받아서 테이블 정보와 내가 보여주고 싶은 컬럼을 정해서 보내주면
 # 거기에 맞게 form을 만들어서 넘겨줌 (form은 html코드로 넘겨줌!)
```

```html
<!-- create.html -->
<body>
    <h1>Movie Create</h1>
    
    <form>
        {{ movie_form }} <!-- create함수에서 가져온 movie_form변수는 입력하는 칸에 대한 html코드가 담겨져있다. -->
        <input type="submit" value="Submit"/>
    </form>
</body>
```

