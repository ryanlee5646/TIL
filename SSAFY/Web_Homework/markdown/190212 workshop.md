1. **django.contrib.auth.forms  안에 있는 UserCreationForm을 활용하여 회원가입 페이지 구성**

```python
# models.py
Class User(models.Model):
    user = models.ForeignKey

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

# view.py
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == 'POST'
    signup_form = CustomUserCreationForm(request.POST) #원래는 UserCreationForm()이나 forms.py에서 새로 forms를 적용해준걸 갖다씀
        if signup_form.is_valid():
            user = signup_form.save()   
            Profile.objects.create(user=user) # User의 Profile생성 (models.py에서 Profile import)

            auth_login(request, user) # 회원가입을 하면 로그인 된 상태로
            return redirect('posts:list')
    else:
        signup_form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})
```

```html
{% extends 'base.html' %}

{%  block container %}

<h1>회원 가입</h1>

<form method="POST">
    {% csrf_token %}
    {{ signup_form }}
    <input type="submit" value="Submit"/>
</form>

{% endblock %}
```

