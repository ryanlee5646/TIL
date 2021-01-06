1. **Django에서는 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹사이트에 요청하게 하는공격을 막는기능을 기본적으로 동작시킨다. 위의공격은 어떤걸 의미하는가?**

`CSRF: 사이트 간 요청 위조(Cross-site Request Forgery)`

`{% csrf_token %}` 코드를 입력하면 공격을 막아준다.



2. **기본적으로 Django에서 views.py에 함수들을 정의할때 request 인자값을 넣어줘야 한다. request를 활용해서 아래의 폼을 통해서 들어온 데이터를 가져오는 코드를 작성하세요.**

```html
<form action="create" method="post">
    {% csrf_token %}
    <input type="text" name="title"/>
    <input type="text" value="Submit"/>
</form>
```

```python
def create(request):
    title = request.POST.get('title')
    post = Post(title=title)
    post.save()
```



3. **다음은 사용자가 이미 작성한 글을 수정하기 위해서 기존의 글을 보여주는 edit페이지를 위한 views.py의 코드이다.**

```python
def edit(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'board/edit.html', {'post':post})
```



​	**아래의 코드에 기존의 데이터를 보여줄 수 있도록 코드를 수정하세요.**

```html
<form action="/posts/{{ post.id }}/update/" method="post">
    {% csrf_token %}
    <input type="text" name="title" value="{{ post.title }}"/>
    <input type="text" name="content" value="{{ post.content }}"/>
    <input type="submit" value="Submit"/>
</form>
```

