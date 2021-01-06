1. **model.py**

```python
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    
    #def __str__(self):
        #return self.title
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    content = models.CharField(max_length=100)
    votes = models.IntegerField()
```



2. **menu.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1> {{ question.title }}</h1>
    <ul>
        {% for choice in choices %}
        <li>{{ choice.content }} : {{ choice.votes }}표</li>
        {% endfor %}
    </ul>
</body>
</html>
```

3. **view.py**

```python
from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your 	views here.
def menu(request):
    question = Question.objects.first()
    choices = question.choice_set.all()
    return render(request, 'menu.html', {'question':question, 'choices':choices})
    
```



4. **urls.py**

```python
from django.urls import path
from . import views

app_name = 'votes'

urlpatterns = [
    path('menu/', views.menu, name='menu'),
]
```

