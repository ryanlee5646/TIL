## MVC(MTV)

M - Model(models.py)

V - View(Template.html)

C - Controller(views.py)



## MVVM

M - Model : 아직없음

V - View(HTML) : 

VM - View-Model(Vue)



## Django

```python
# 조건
{% if post.is_public %}
	{{ post }}
{% endif %}

# 반복
{% for post in posts %}
	{{ post}}
{% endfor %}
```



## Vue Directive(디렉티브)

```html
<!-- 조건 -->
<p v-if="post.isPublic">
    {{ post}}
</p>
<!-- 반복 -->
<ul>
    <li v-for="post in posts">
    	{{ post }}
    </li>
</ul>
```

