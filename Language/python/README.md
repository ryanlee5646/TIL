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

#### 1.`*args` 

* Python에서 함수을 생성할 때 가변의 인자값(argument)을 받고 싶을 때 사용

* `*args`에 속한 인자값들은 튜플(tuple) 형태로 넘어온다.

```python
def plus (a, b , *args):
  print(args)
  
  return a + b

plus(1,2,3,3,3,3,3,3,3,3)

>>> (3, 3, 3, 3, 3, 3, 3, 3)
  
```

#### 2. `**kwargs`

* `*args` 와 같이 가변의 인자값을 받고 싶을 때 사용한다. 다만 keyword 형태로 인자값을 받을 때 사용한다.

* `**kwargs` 에 속한 인자값들은 딕셔너리(Dictionary) 형태로 넘어온다.

```python
def plus (a, b, **kwargs):
  print(kwargs)
  
  return a + b

plus(1,2, hello=True, aa=True, bb=True)

>>> ('hello':True, 'aa':True, 'bb':True)
```



### Function과 Method의 차이

#### 1. Function

* 클래스(Class) 바깥에서 선언된 함수
* 클래스의 메서드(Method)처럼 객체의 Instance를 첫번째 인자(argument)로 받지 않아도 됨(인자가 없어도됨)

```python
class Car(): 
  wheel = 4
  door = 4
  sheet = 4
  window = 4

def start():	# Function:  
  a = 20
  print(a)
  
start()
>>> 20
```

#### 2. Method

* 클래스(Class) 안에 선언된 함수
* 함수의 인자값 없이 호출 하더라도 함수를 선언할 때 첫번 째 인자값을 넣어서 선언해 주어야 한다
* 클래스의 메서드는 자신을 호출한 객체의 인스턴스가 첫번 째 인자값이 되기 때문이다.

```python
class Car(): 
  wheel = 4
  door = 4
  sheet = 4
  window = 4

  def start(self):	# Method: self = proche라고 봐도 무방하다 
    self.door = 2
    print(self.door)
    
porche = Car()
porche.start()

>>> 2
    
```



### 객체의 개념

#### 1. 클래스 선언

```python
class Car():
    
    def __init__(self, **kwargs): # Class가 실행될 때 바로 만들어지는 메서드는 __init()
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black") # kwargs.get(key, default)
        self.price = kwargs.get("price", "$20") # 가변의 인자를 받아와서 커스터마이징 가능
    
    def __str__(self): # Overiding
        return f"Car with {self.wheels} wheels"

porche = Car(color="green", price="$40")
print(porche.color, porche.price)

>>> green $40

mini = Car()
print(mini.color, mini.price)

>>> black $20

```

#### 2. 클래스 상속(오버로드, 오버라이딩)

```python
class Car():
    
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black") # kwargs.get(key, default)
        self.price = kwargs.get("price", "$20")
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"

# Car 클래스를 상속
class Convertible(Car):

    def __init__(self,**kwargs): 
        # super()을 선언하면 부모클래스의 메서드를 오버로드, 선언하지 않으면 오버라이드(새롭게 메서드 선언) 
        super().__init__(**kwargs) # **kwarg를 선언하지 않으면 default값, 선언하면 객체 생성시 넘겨준 argument값을 받아옴
        self.time = kwargs.get("time", 10)

    def take_off(self):

        return "taking off"        

    def __str__(self):
        return f"Car with no roof"


porche = Convertible(color="green", price="$40")
mini = Car()

print(porche.color, porche.price)
>>> "green" "$40"
porche.take_off()
```

