1. **Class모델과 Student모델을 1:N관계로 설정하려고 한다. models.py에 넣어야하는 코드를 작성하세요. (1:N 관계중 N의 클래스를 작성해주세요.)**

```python
class Student(models.Model):
    class = models.ForeignKey(Class, on_delete=models.CASCADE)
```



2. **Question모델과 Comment모델은 1:N관계를 가지고있다. A = Question.objects.get(id=id) 위의 코드가 있을때 views.py에서 Comment를 모두 가져오기 위한 코드를 작성하세요. (related_name 은 설정하지 않았다고 가정한다.)**

```python
A.comment_set.all()
# related_name='comments'
A.comments.all()
```





3. **기본적으로 1:N관계를 설정을 할 때 ForeignKey를 이용해서 1에 해당하는 클래스를 지정해준다. 지정한 클래스가 Movie일 때 ForeignKey로 지정된 컬럼의 이름은 무엇인가?**

```python
movie 
```

