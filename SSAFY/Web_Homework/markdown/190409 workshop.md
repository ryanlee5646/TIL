1. **게시물의 해시태그를 구현하기 위하여 아래와 같이 객체-관계다이어그램을 작성하였다. 다이어그램을 바탕으로models.py 에 Post모델과 Hashtag모델을 정의해본다.**

```python
class Post(models.Model):
    title = models.CharField(max_length=100) # 의사정보
	content = models.TextField()
    hashtags = models.ManyToManyField(Hash, related_name='post', blank=True)

# Doctor:Patient = 1:N
class Hash(models.Model):
    content = models.TextField()
    
```

