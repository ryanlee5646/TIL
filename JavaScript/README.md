### javascript 수의 연산

1. `Math.pow(3,2);` : 9, // 3의 제곱(3의 2승)
2. `Math.round(10.6);`: 11, // 10.6을 반올림
3. `Math.ceil(10.2);`: 11, // 10.2를 올림
4. `Math.floor(10.6);`: 10, // 10.6을 내림
5. `Math.sqrt(10.6);`: 3,  // 3의 제곱근()

6.  `Math.random()`: 0부터 1.0 사이의 랜덤한 숫자

* `Math.round(100 * Math.random())` : 0과 1사이의 랜덤한 수에 100을 곱한 소수자리를 반올림함



### 비교연산자 `==`(동등연산자) 와 `===`(일치연산자)

* 비교연산자 `==` 는 데이터 type과 관계없이 형태가 같으면 `True`
  * `1 == '1'` == `True`
* 일치연산자 `===` 는 데이터 type까지 일치해야 `True`
  * `1 == '1'` == `False`

=> 작업을 할때 일치연산자는 안쓰는 것을 권장! 무조건 일치연산자를 쓰는 것이 나중에 코드오류가 나지 않는다.



### alert와 prompt

`alert` : 알림창을 띄움

`prompt`: 입력창이 있어서 사용자로부터 입력한 정보를 받을 수 있음



### 논리연산자 And('&&') 와 Or('||')

```html
<script>
        id = prompt('아이디를 입력해주세요.');
        password = prompt('비밀번호를 입력해주세요.');
        
        if ((id === 'egoing' || id === 'ymbrdii2002' || id === 'ryanlee5646') && password === 'rbwlsl91' ){
            alert ('인증 했습니다.');
        } else {
            alert('인증에 실패 했습니다.')
        }
    </script>
```

코드 앞에 `!` 을 붙이면 not의 의미를 가진다.



### Javascript에서 True와 False로 간주하는 데이터

1. 숫자 `1` 은 True   `0` 은 Flase

2. 빈문자열

3. ```html
   if(!''){
   	alert('빈 문자열')
   }
   
   ```

3. **Undefiend**

4. **Null**
5. 값이 할당되지 않은 변수
6. !NaN 



### docoumet.write

=> 자바스크립트를 이용해서 웹페이지에 텍스트를 출력할 때 쓰는 메서드

```html
<script>
    document.write('Coding everybody <br />')
</script>
```



### Javascript 함수 (Function)

* 함수는 코드의 재사용성을 높여준다.

```javascript
/* 함수 정의 방법 1 */
        numbering = function (){
            i = 0;
            while(i < 10){
                document.write(i);
                i += 1;
            }
        }
        numbering();

        /* 함수 정의 방법 2 */
        function numbering() {
            i = 0;
            while(i < 10){
                document.write(i);
                i += 1;
            }
        }
        numbering();
        
        /* 함수 정의 방법 3(익명함수) */
        (function (){
            i = 0;
            while(i < 10){
                document.write(i);
                i += 1;
            }
        })();
```



#### 배열(Array)

=> 배열(array)이란 연관된 데이터를 모아서 통으로 관리하기 위해서 사용하는 데이터 타입



### Javascript  값을 추가하는 메서드

```java
data = ["a", "b", "c", "d", "e"]

// push()
data.push('f');
=> ["a", "b", "c", "d", "e", "f"]

// concat() 배열을 맨뒤에 삽입
data.concat(['h','i']);
=> ["a", "b", "c", "d", "e", "f", "h", "i"]

// unshift() 맨 앞에 삽입
data.unshift('z');
=> ["z","a", "b", "c", "d", "e", "f", "h", "i"]

// splice()

```



#### Splice() 메서드

| 인자명                | 데이터형 | 필수/옵션 | 설명                                                         |
| --------------------- | -------- | --------- | ------------------------------------------------------------ |
| index                 | number   | 필수      | 배열에 추가할 특정 배열의 위치를 가르키는 index              |
| howmany               | number   | 필수      | index에서부터 제거될 원소들의 수. index부터 index+howmany에 해당하는 원소들은 삭제된다. 이 값이 0이면 어떠한 원소도 삭제되지 않는다. |
| element1,...,elementN | number   | 옵션      | index와 index+howmany 사이에 추가될 값                       |

```javascript
var numbers = [1,2,3,4,5,6,7,8,9,10];
alert(numbers.splice(2)); // array, [3,4,5,6,7,8,9,10], 시작점 2부터 배열의 마지막 원소까지를 대상으로 한다.
alert(numbers); // array, [1,2], 원본이 수정된다. 
 
var numbers = [1,2,3,4,5,6,7,8,9,10];
alert(numbers.splice(2, 4)); // array, [3,4,5,6]
 
var numbers = [1,2,3,4,5,6,7,8,9,10];
alert(numbers.splice(2, 4, 'three', 'four', 'five', 'six')); 
// array, [3,4,5,6] 추출되는 배열이 출력됨
alert(numbers); // array, [1,2,three,four,five,six,7,8,9,10]
```



### javascript 값을 제거하는 메서드

```javascript
var numbers = [1,2,3,4,5,6,7,8,9,10];

numbers.shift(); // 가장 왼쪽에 값을 제거 후 출력
1
numbers
(9) [2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.pop() // 가장 오른쪽에 값을 제거 후 출력
10
numbers
(8) [2, 3, 4, 5, 6, 7, 8, 9]
```



### javascript 값을 정렬하는 메서드

```javascript
var li = ['c','e','a','b','d']

li.sort(); // 배열의 값을 순서대로 정렬
(5) ["a", "b", "c", "d", "e"]

li.reverse() // 현재 배열의 값을 역순으로 정렬
(5) ["e", "d", "c", "b", "a"]
```



### 객체(Object)

=> 배열은 아이템에 대한 식별자로 숫자를 사용했다. 데이터를 추가하게 되면 배열 전체에서 중복되지 않는 인덱스가 자동으로 만들어져서 추가된 데이터에 대한 식별자가 된다. 이 인덱스를 이용해서 데이터를 가져오게 되는 것이다. 만약 인덱스로 문자를 사용하고 싶다면 객체(Dictionary)를 사용해야 한다. 다른 언어에서는 연관배열(Associative array) 또는 **맵(map)**, **딕셔너리(Dictionary)**라는 데이터 타입이 객체에 해당한다.

```javascript
// 객체 생성 방법 1
var grade = {'egoing':10, 'ryan': 30, 'gyujin': 80}

// 객체 생성 방법 2
var grades = {} ;
grades['egoing'] = 30
grades['gyujin'] = 80
grades
{egoing: 30, gyujin: 80}


//객체 호출 방법
grades.egoing
30
grades["egoing"]
30
grades['eg'+'oing']
30
```



### 객체(Object)의 반복문(for)

```javascript
var grades = {'egoing': 10, 'ymbrdii2002': 30, 'gyujin': 50};

for(key in grades) {
  document.write("key: " + key + " value: " + grades[key] + "<br>")
}
key: egoing value: 10
key: ymbrdii2002 value: 30
key: gyujin value: 50

// 배열 for문
var a = [1,2,3,4,5]
for(var name in a){
    console.log(a[name])
}
```



### Javascript 객체지향 프로그래밍

* `this` 는 정해져있는 변수로, 특정 함수가 속해있는 객체의 변수를 뜻함(grades)

```javascript

var grades = {
  'list' : {'egoing': 10, 'gyujin': 80, 'ryan': 35},
  'show' : function(){
    for(var name in this.list){ // 객체가 가지고있는 키값 'list'의 value값을 차례로 뽑아냄
      console.log(name, this.list[name]);
    }
  }
}
grades['show']();
grades.show();

```



### Javascript 모듈화(Module)

* 하나의 코드를 여러개의 파일로 분리하는 것이다.
  * 자주 사용되는 코드를 별도의 파일로 만들어서 필요할 때마다 재활용할 수 있다.
  * 코드를 개선하면 이를 사용하고 있는 모든 애플리케이션의 동작이 개선된다.
  * 코드 수정 시에 필요한 로직을 빠르게 찾을 수 있다.
  * 필요한 로직만을 로드해서 메모리의 낭비를 줄일 수 있다.
  * 한번 다운로드된 모듈은 웹브라우저에 의해서 저장되기 때문에 동일한 로직을 로드 할 때 시간과 네트워크 트래픽을 절약 할 수 있다. (브라우저에서만 해당)



### 모듈이란

순수한 자바스크립트에서는 모듈(module)이라는 개념이 분명하게 존재하지는 않는다. 하지만 자바스크립트가 구동되는 호스트 환경에 따라서 서로 다른 모듈화 방법이 제공되고 있다. 이 수업에서는 자바스크립트의 대표적인 호스트 환경인 웹브라우저에서 로직을 모듈화하는 방법에 대해서 알아볼 것이다.

##### 호스트 환경이란?

호스트 환경이란 **자바스크립트가 구동되는 환경**을 의미한다. 자바스크립트는 브라우저를 위한 언어로 시작했지만, 더 이상 브라우저만을 위한 언어가 아니다. 예를들어 [node.js](http://nodejs.org/about/)는 서버 측에서 실행되는 자바스크립트다. 이 언어는 자바스크립트의 문법을 따르지만 이 언어가 구동되는 환경은 브라우저가 아니라 서버측 환경이다. 또 구글의 제품 위에서 돌아가는 [Google Apps Script](https://developers.google.com/apps-script/) 역시 자바스크립트이지만 google apps script가 동작하는 환경은 구글 스프레드쉬트와 같은 구글의 제품 위이다. 여러분은 자바스크립트의 문법을 이용해서 PHP와 같은 **서버 시스템을 제어(node.js)**하거나 **구글의 제품(Google Apps Script)을 제어** 할 수 있다. 지금 당장은 어렵겠지만, 언어와 그 언어가 구동되는 환경에 대해서 구분해서 사고 할 수 있어야 한다. 이를 위해서는 다양한 언어를 접해봐야 한다.



### Javascript 모듈화

```javascript
// main.html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

    <script src="greeting.js"></script>
</head>
<body>
    <script>
        alert(welcome());
    </script>
</body>

// greeting.js

function welcome(){
    return 'Hello world'
}

```

* `greeting.js` 의 있는 함수를 끌어다 쓰기위해서는 `main.html` 의 **`<head>`** 태그 아래에 

  `<script src="greeting.js"></script>` 형식으로 호출해준다.



### 라이브러리(Library)

라이브러리는 모듈과 비슷한 개념이다. 모듈이 프로그램을 구성하는 작은 부품으로서의 로직을 의미한다면 **라이브러리는 자주 사용되는 로직을 재사용하기 편리하도록 잘 정리한 일련의 코드들의 집합을 의미**한다고 할 수 있다. 

Javascript 대표적인 모듈인 **jQuery**

**URL** : http://jquery.com

**Manual**: http://api.jquery.com



**jQuery** **사용방법**

```javascript
    <script src=jquery.js></script>  //jQuery 모듈을 호출
</head>
<body>
    <ul id='list'>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>

    <input type="button" value="execute" id="execute_btn">
    <script>
        $('#list li').text('coding everybody') // <li> 태그 사이에 text를 삽입하는 모듈
        
        $('#execute_btn').click(function(){ // 버튼을 클릭하면
            $('#list li').text('hello world'); // <li> 태그 사이에 text를 삽입
        })
    </script>
```

* jQuery의 처음 시작은 무조건 `$` 로 시작한다.
* 선택자(Selector) 접근 할때는 선택자 고유의 접근 기호를 사용하고 한칸을 띄운후 내부 태그명으로 접근