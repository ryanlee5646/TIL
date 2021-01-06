1.

2.

```python
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #1:N
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
```



