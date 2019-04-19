### 1. TemplateSyntaxError

=>대부분 html 파일에서 {} 중괄호 오류

ex) {% load bootstrap4 %}

### 2. Forbidden error

=> {% csrf_token %} 이 빠진 에러 

### 3. Page not found(404)

=> 링크에 걸려있는 주소경로가 잘못됐거나/ 그 주소경로가 실제로 없거나!

url.py는 주소를 뒤에 꼭 닫아줘야하고  html에서는 시작부터 끝까지 다 /해줘야함

(그냥 html에서 url 이름으로 접근하는게 좋을듯 {% url 'posts:create' %})

### 4. NameError

=> 변수명이 잘못된 경우.(무조건 파이썬 문제이기 때문에 views.py를 보면됌)

ex) name 'user' is not defined

### 5. IntegrityError

=> Not Null constraint failed: posts_comment.post_id

`comment_post_id = post_id` 에 post_id가 없어서 값이 비어서 나는 에러



### 6. 페이지가 작동하지 않습니다.

@require_POST

페이지에 에러를 파악할수없으면 Bash로 이동해서 파악

Get 방식으로 받으면 안되는데 get방식으로 받았을때 @require_POST추가해야함

(주소바에서 뭘입력했는지 내용이 보이면 get방식임)



### 7.  NoReverseMatch at /posts/

해당하는 주소(매칭되는 주소가 없다) ##이름매칭이 중요!!

django내에서 url에 이름을 지어줫는데 우리가 지어준 이름에 comment가 없다.

확인해야할 곳:  urls.py 에 url name에 comment가 있는지 확인

html에서 post:comment에서 comment이름을 잘못 지정했거나

comment를 생성하는 곳으로 넘겨줘야해서 url 이름이 comment_create였다. 



### 8. 서버실행이 안될때 Bash에서 

class PostForm에서 

django.core.exceptions.FieldError: Unknown field(s) (title) 에러는

form.py에서 Meta class에서 fields 이름이 models.py와 매칭이 되는지를 봐야함



### 9. Models.py에서 테이블을 수정했을때

데이터 값이 있는 상태에서 새로은 column을 추가하게 되면 기존 레코드에 새로추가된 열에는 어떻게 처리할건지 묻는 메세지가 나옴

```python
class Article(models.Model):
	title = models.TextField()
    content = models.TextField()
# 젤 올바른 방법은 메세지에서 빠져나가기를 해서 
# 함수 인자값에 
(blank=True)를 추가해주고 다시 migrations을 해주는게 좋다
#다른방법은
# Bash에서 만약 1번을 선택햇으면 어떤 값을 넣을거냐 물을때 ''
```

게시판에 어떤 사람이 와서 글을쓰고 제목 내용 입력 후 서브밋 눌러서 디데일 페이지로 들어갔는데

제목에만 값이 드간다.

### 10. 로직에러

만약 base.html에 있는 {%  block container %}에 block 과 list.html에 있는 {% container %} 이름이 다르다면

출력되지 않음 

```html
{% extends 'base.html' %}

{% block container %}

{% endblock %}

```



### 11. Settings.py 언어/시간 설정

```python
LANGUAGE_CODE = 'ko-kr' /'en-us'

TIME_ZONE = 'Asia/Seoul' /'UTC' 

USE_I18N = True # 언어설정을 할건지 말건지 (만약 False라면 어떤언어로 변경해도 적용 x)

USE_L10N = True # 이건 필요없음

USE_TZ = True # 타임존을 설정할건지 말건지
```

