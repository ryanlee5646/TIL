1. **Django는 요청에 대한 응답을 해줄때 허용하는 도메인에게만 응답을 해주도록 설정한다. Settings.py 파일에서 도메인을 허용하기 위해 수정해줘야하는 변수이름을 찾아서 적어주세요.**

```python
ALLOWED_HOSTS = ['playground-ryanlee5646.c9users.io']
```



2. **https://<your-server-url>/ssafy 로 요청이 들어왔을때 응답을 해주기위해 urls.py에 추가해 주어야할 코드를 작성하세요.(실행하는 함수는views.py안에 있는 ssafy 함수라고 가정한다.)**

```bash
from django.contrib import admin
from django.urls import path
from pages import views
urlpatterns = [
    path('ssafy/', views.ssfay),
    path('admin/', admin.site.urls),
]
```



3. **Django 서버를 실행시키는 명령어를 작성해주세요.(C9환경에서)**

```bash
 python manage.py runserver $IP:$PORT
```



4. **django는 MTV로 이루어진 web framework 이다. MTV가 무엇의 약자인지 작성하세요.**

```bash
M:Model
T:Template
V:View
```

