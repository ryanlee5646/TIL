1. **학생들의 이름과 나이를 저장하기위한 폼클래스를 정의하려고 한다. 다음과 같이 Student모델이 선언되있다고 가정할때 어울리는 StudentForm클래스를 작성하세요.**

```python
from django import forms

# 그냥 Form
class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    
# Model Form
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fileds = ['name', 'age']
        #fields = '__all__' (Student에 있는 모든 field들을 가져오고 싶을때) 
        
```



2. **위에서 만든 폼클래스를 활용해 템플릿에서 활용하려고 한다. views.py의 코드가 다음과 같을때 new.html에서 사용자가 데이터를 입력할 수 있도록 코드를 작성하세요. (사용자가 데이터를 입력하고 submit버튼을 누르면/students/create/ 로 요청을 보내고 method는 post방식이다.)**

```html
<form action="/students/create/" method="post">
        {% csrf_token %}
        <div>
            {{ form.errors }} <!-- error messages (ul, li tag) -->
            {{ form.name.label_tag }} <!-- label tag -->
            {{ form.name }}    <!-- input tag -->
        </div>
        <!-- 2.content -->
        <div>
            {{ form.age.errors}}
            {{ form.age.label_tag}}
            {{ form.age }}
        </div>
            <!--{{ form }}-->
        <input type="submit" value="Submit"/>
    </form>
    </form>
```

