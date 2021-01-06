from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    
    def __str__(self):
        return self.title
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey 외부테이블의 id값을 저장
    content = models.CharField(max_length=100)
    votes = models.IntegerField()