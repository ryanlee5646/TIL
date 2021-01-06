```python
# urls.py
from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('', views.PersonList.as_view(), name='list'),
]
```



```python
# views.py
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# def list(request):
    # person = Person.objects.all()
    # return render(request, 'person/person_list.html', {'person': person})
    
class PersonList(ListView):
    model = Person
    context_object_name = 'person'
  
```



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
    <h1> Person List</h1>
    <a href="{% url 'person:create' %}">New Person</a>
    <ul>
        {% for p in person %}
        <li>
            {{ p.last_name }} - {{ p.email }} - {{ p.age }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

