# Python Note

> python에 대해 새롭게 알게된 내용을 기록하기 위한 노트



[2021.01.20]

### String 메소드

#### 1. title()

각 단어의 첫글자를 대문자로 바꿔주는 메소드

```python
string = "hello pyton"
print(string.title())
>>> "Hello Python"
```



[2021.01.23]

### Python 함수 가변의 Argument

1. `*args` : Python에서 함수을 생성할 때 가변의 인자값(argument)을 받고 싶을 때 사용
   * `*args`에 속한 인자값들은 튜플(tuple) 형태로 넘어온다.

```python
def plus (a, b , *args):
  print(args)
  
  return a + b

plus(1,2,3,3,3,3,3,3,3,3)

>>> (3, 3, 3, 3, 3, 3, 3, 3)
  
```

2. `**kwargs`: `*args` 와 같이 가변의 인자값을 받고 싶을 때 사용한다. 다만 keyword 형태로 인자값을 받을 때 사용한다
   * `**kwargs` 에 속한 인자값들은 딕셔너리(Dictionary) 형태로 넘어온다.

```python
def plus (a, b, **kwargs):
  print(kwargs)
  
  return a + b

plus(1,2, hello=True, aa=True, bb=True)

>>> ('hello':True, 'aa':True, 'bb':True)
```



