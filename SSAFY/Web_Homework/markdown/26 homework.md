**1.Django Form을 활용하기 위해서 클래스를 만들때 장고 내부에만 들어져있는 클래스를 상속받아서 활용해야 한다. 이 클래스를 import 하는 문장을 작성하세요.**

```python
from django import forms
```



 

**2.폼클래스를 템플릿에서 활용하기 위해서 form이라는 이름으로 템플릿 페이지로 전달하였다. 템플릿 페이지에서 form을 <p>태그들로 감싸서 렌더링하기 위한 코드를 작성하세요.**

```html
{{ form.as_p }} <!-- p -->
{{ form.as_ul }} <!-- li -->
{{ form.as_table }} <!-- tr -->
```





**3.폼클래스를 활용할 때 폼에 담긴 데이터가 유효한지 체크하기 위해서 is_valid()메소드를 활용한다. is_valid()메소드를 통과하고 나서 사용자의 데이터를 가져오기 위해서 빈칸에 들어가야 할코드를 작성하세요.**

```python
form.cleaned_data.get('name')

form.cleaned_data['name']
```



