1. **Question모델과 Comment 모델이 1:N관계라고 할 때 하나의 Question을 보여주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html이 있을 때 모든Comment의 content를 h3태그를 이용해서 출력하는 for문을 작성하세요.(related_name은 설정해주지 않았다고 가정한다.)**

```html

{% for comment in question.comment_set.all %}
<h3>{{ comment.content }}</h3>
{% endfor %}
```





2. **다음과 같은 urls.py파일이 있다고 가정할 때 comment를 작성하는 버튼을 만들기 위해form태그 안에 action속성값으로 넣어줘야 하는 경로를 작성하세요.**

```pyhon
action="/question/{{ question.pk }}/comments/create" (기존경로 직접입력)

{% url 'question:comments_create' question.pk %}
```

