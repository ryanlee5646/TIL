**1.**

파이썬은 객체지향 프로그래밍언어입니다.
파이썬에서 기본적으로 정의된 클래스 5개만 작성해보세요.

**int, dict, complex(복소수),  list,  float, set**

**2.**

아래의 코드에서 x의데이터타입을 확인하고자 할 때, 기본적으로type(x) == int로 비교할 수 있다.

​                                          **`x=3**`

뿐만아니라 클래스–인스턴스 관계를 활용하여 확인할 수도 있는데,이 때 사용되는 함수를 작성해보세요. 

​                          **`isinstance(x,int)**`

**3.**

우리가 지금껏 문자열, 리스트, 딕셔너리 등을 조작할 때 활용하였던것은 모두 클래스에 정의된 메소드를 활용한 것이다. 예를 들면, 리스트를 정렬할때 다음과 같이 코드를 작성할 수 있다.

```python
numbers = [5,1,2]
number.sort
print(numbers)
```

이처럼 지금껏 활용했던 문자열, 리스트, 딕셔너리 메소드중 3가지 만 작성 해보세요.

**`.append(x) , .insert(i, x), .remove(x), .count(x)`**

**4.**

각각의 인스턴스들은 데이터 어트리뷰트(data attribute)를 가지고있다. 다음의 코드는 복소수의 허수부의 값을 확인할 수 있으며, 이는 복소수클래스(complex)면 모두 가지고 있다.

```python
num = 3+4j
num.imag
```

변수 num의 실수부를 출력하는 코드를 아래에 작성해보고,메소드호출과 차이점을 확인해보자.

​                                      **`num.real`**

메소드 호출은 .sort() 처럼 괄호안에 인스턴스를 넘겨주고 클래스 내부에 함수로 정의되어 있고, num.real or num.imag처럼 변수를 할당 할 수없다