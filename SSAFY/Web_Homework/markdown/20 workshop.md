**설문앱을 만들려고 한다.이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇표를 받았는지 저장하는 기능을 가지고있다. 설문앱은 Question모델과 Choice모델을 가지고 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N관계를 가지고 있다.**

```python
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey 외부테이블의 id값을 저장
    content = models.CharField(max_length=100)
    votes = models.IntegerField()
```

