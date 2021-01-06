1. **Django에서 선언한 Model을 실제DB에 반영하는 과정을 무엇이라고 하는가?**

  `migration` (`makemirgrations`, `migrate`)

2. **모델의 필드를 정의할 때 CharField는 필수로 들어가야하는 인자가 존재한다. 무엇인가?**

  `max_length`

3. **Django 에서 동작하는 모든명령을 대화식 Python쉘에서 시험할 수 있는명령어를 작성하세요.**

  `python manage.py shell `

4. **Post라는 이름의 모델은 CharField로 정해진 title과 CharField로 정해진content가 필드로 정의되어 있다. 제목은 자신의 이름, 내용은 자신의 이메일 정보가 들어간 Post를 만드는 코드를 작성하세요.**

* Creat

```python
post = Post(title='ryanlee5646', content='ryanlee5646@gamail.com')
post.save()
```



  