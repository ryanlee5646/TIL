**7/21(일) TIL**

### javascript 수의 연산

1. `Math.pow(3,2);` : 9, // 3의 제곱(3의 2승)
2. `Math.round(10.6);`: 11, // 10.6을 반올림
3. `Math.ceil(10.2);`: 11, // 10.2를 올림
4. `Math.floor(10.6);`: 10, // 10.6을 내림
5. `Math.sqrt(10.6);`: 3, // 3의 제곱근()
6. `Math.random()`: 0부터 1.0 사이의 랜덤한 숫자

- `Math.round(100 * Math.random())` : 0과 1사이의 랜덤한 수에 100을 곱한 소수자리를 반올림함

### 비교연산자 `==`(동등연산자) 와 `===`(일치연산자)

- 비교연산자

   

  ```javascript
  ==
  ```

   

  는 데이터 type과 관계없이 형태가 같으면

   

  ```javascript
  True
  ```

  - `1 == '1'` == `True`

- 일치연산자

   

  ```javascript
  ===
  ```

   

  는 데이터 type까지 일치해야

   

  ```javascript
  true
  ```

  - `1 == '1'` == `False`

=> 작업을 할때 일치연산자는 안쓰는 것을 권장! 무조건 일치연산자를 쓰는 것이 나중에 코드오류가 나지 않는다.

### alert와 prompt

`alert` : 알림창을 띄움

`prompt`: 입력창이 있어서 사용자로부터 입력한 정보를 받을 수 있음

### 논리연산자 And('&&') 와 Or('||')

```javascript
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

1. 숫자 `1` 은 True `0` 은 Flase

2. 빈문자열

3. ```javascript
   if(!''){
   	alert('빈 문자열')
   }
   ```

4. **Undefiend**

5. **Null**

6. 값이 할당되지 않은 변수

7. !NaN

### docoumet.write

=> 자바스크립트를 이용해서 웹페이지에 텍스트를 출력할 때 쓰는 메서드

```javascript
<script>
    document.write('Coding everybody <br />')
</script>
```

### Javascript 함수 (Function)

- 함수는 코드의 재사용성을 높여준다.

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

**7/22(화) TIL**

### Javascript 값을 추가하는 메서드

```javascript
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
(9) [2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.pop() // 가장 오른쪽에 값을 제거 후 출력
10
numbers
(8) [2, 3, 4, 5, 6, 7, 8, 9]
```

### javascript 값을 정렬하는 메서드

```javascript
var li = ['c','e','a','b','d']

li.sort(); // 배열의 값을 순서대로 정렬
(5) ["a", "b", "c", "d", "e"]

li.reverse() // 현재 배열의 값을 역순으로 정렬
(5) ["e", "d", "c", "b", "a"]
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

**7/23(화) TIL**

### Javascript 객체지향 프로그래밍

- `this` 는 정해져있는 변수로, 특정 함수가 속해있는 객체의 변수를 뜻함(grades)

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

- 하나의 코드를 여러개의 파일로 분리하는 것이다.
  - 자주 사용되는 코드를 별도의 파일로 만들어서 필요할 때마다 재활용할 수 있다.
  - 코드를 개선하면 이를 사용하고 있는 모든 애플리케이션의 동작이 개선된다.
  - 코드 수정 시에 필요한 로직을 빠르게 찾을 수 있다.
  - 필요한 로직만을 로드해서 메모리의 낭비를 줄일 수 있다.
  - 한번 다운로드된 모듈은 웹브라우저에 의해서 저장되기 때문에 동일한 로직을 로드 할 때 시간과 네트워크 트래픽을 절약 할 수 있다. (브라우저에서만 해당)

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

- `greeting.js` 의 있는 함수를 끌어다 쓰기위해서는 `main.html` 의 **<head>** 태그 아래에

  <script src="greeting.js"></script> 형식으로 호출해준다.

### 라이브러리(Library)

라이브러리는 모듈과 비슷한 개념이다. 모듈이 프로그램을 구성하는 작은 부품으로서의 로직을 의미한다면 **라이브러리는 자주 사용되는 로직을 재사용하기 편리하도록 잘 정리한 일련의 코드들의 집합을 의미**한다고 할 수 있다.

Javascript 대표적인 모듈인 **jQuery**

**URL** : [http://jquery.com](http://jquery.com/)

**Manual**: [http://api.jquery.com](http://api.jquery.com/)

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

- jQuery의 처음 시작은 무조건 `$` 로 시작한다.
- 선택자(Selector) 접근 할때는 선택자 고유의 접근 기호를 사용하고 한칸을 띄운후 내부 태그명으로 접근

**7/25(목) TIL**

### Javascript 정규표현식(regular expression)

#### 정규표현식 객체 생성자

```javascript
// 이 둘은 같은 표현
var pattern = /a/;
var pattern = new RegExp('a');

console.log(pattern);
// => /a/
```

#### 정규표현식 메서드 실행

**1. RegExp.exec()**

- 인자안에 들어오는 값 중에서 객체안에 문자를 찾는 메서드
- 문자열 뒤에 `.` 이 있으면 다음 오는 문자까지 찾아줌

```javascript
var pattern = /a/

pattern.exec('abcde');
=> 'a'

var pattern = /a./
pattern.exec('abcde');
=> 'ab'
pattern.exec('bcdef');
=> null // 찾고자 하는 문자가 없음
```

**2. RegExp.test()**

- 인자안에 문자열이 있으면 True, 없으면 False값을 반환

```javascript
var pattern = /a/

pattern.test('abcde');
=> true
pattern.test('bcde');
=> false
```

**3. String.match()**

- `RegExp.exec()`와 유사하며 정규표현식 패텬과 일치하는 문자열들을 담고 있는 배열을 리턴
- 해당되는 문자열이 없을 경우 null을 리턴

```javascript
var pattern = /a/
var str = 'abcedf'
str.match(pattern);
=> ["a"]
```

**4. String.replace()**

- 문자열에서 패턴을 검색해서 이를 변경한 후에 변경된 값을 리턴한다.

```javascript
'abcdef'.repalce("a", "A");
=> "Abcdef"
```

### 옵션(Option) - i 와 g

- `i` 는 찾는 문자열의 대소문자 구분없이 리턴

```javascript
var xi = /a/;
console.log("Abcde".match(xi)); // null
var oi = /a/i;
console.log("Abcde".match(oi)); // ["A"];
```

- `g` 는 검색된 모든 결과를 리턴함

```javascript
var xg = /a/;
console.log("abcdea".match(xg)); ["a"]
var og = /a/g;
console.log("abcdea".match(og)); // ["a","a"]
```

- `ig` 형태로 한번에 붙여서 값을 리턴 할 수도 있음

```javascript
"AabcdAa".match(/a/ig);
=> ["A","a","A","a"]
```

### 함수에서 전역변수(Global scope)와 지역변수(Local scope)

1. **전역변수로 선언**

```javascript
var vscope = 'global';
function fscope(){
  alert(vscope);
}
fscope();
// 'global' 출력
```

1. **함수안에 전역변수를 정의**

```javascript
var vscope = 'global';
function fscope(){
  var vscope = 'local' // 지역변수를 선언
  alert(vscope);
}
fscope();
alert(vscope);
// 지역변수 'local' 출력
// 그 다음 전역변수 'global' 출력
```

1. **함수 안에서 전역변수를 재정의**

```javascript
var vscope = 'global';
function fscope(){
  vscope = 'local'
  alert(vscope);
}
fscope();
alert(vscope);
// 'local' 이 2번 출력
```

### 유효범위의 효용성

```javascript
function a (){
  var i = 0;
}
for(var i=0; i<5; i++){
  a();
  document.write(i);
}

// 01234
```

=> 전역에다가 변수를 선언하고 for문을 돌렸지만 함수 안에 같은 이름의 지역변수를 선언하였다고 해서 영향을 주지 않음.

```javascript
function a (){
  i = 0;
}
for(var i=0; i<5; i++){
  a();
  document.write(i);
}

// 무한루프
```

=> 이 경우에는 함수안에서 전역변수를 계속 0으로 초기화하기 때문에 **무한루프**에 빠짐, 그러므로 전역변수를 지역변수와 같게 지정하면 이러한 오류를 범할 수 가 있음.

### 전역변수의 사용 (모듈화)

```javascript
// 하나의 전역변수를 사용
var MYAPP = {}
MYAPP.calcurator = {
  'left' : null,
  'right' : null
}
MYAPP.coordinate = {
  'left': null,
  'right': null
}
console.log(MYAPP)
MYAPP.calcurator.left = 10;
MYAPP.calcurator.right = 20;
function sum(){
  return MYAPP.calculator.left + MYAPP.calcurator.right;
}
document.write(sum());
```

=> 하나의 전역변수 객체에 하위에 전역변수들을 관리하게 되면, 변수 충돌이 일어나는 것을 방지할 수 있다.

```javascript
function myappfn(){
  var MYAPP = {}
  MYAPP.calcurator = {
    'left' : null,
    'right' : null
  }
  MYAPP.coordinate = {
    'left': null,
    'right': null
  }
  console.log(MYAPP)
  MYAPP.calcurator.left = 10;
  MYAPP.calcurator.right = 20;
  function sum(){
    return MYAPP.calculator.left + MYAPP.calcurator.right;
  }
  document.write(sum());
}
myappfn();
```

=> 함수를 선언했지만 함수명을 지정하는 것 역시 하나의 전역변수를 사용하는 것과 동일하다.

```javascript
(function(){
  var MYAPP = {}
  MYAPP.calcurator = {
    'left' : null,
    'right' : null
  }
  MYAPP.coordinate = {
    'left': null,
    'right': null
  }
  console.log(MYAPP)
  MYAPP.calcurator.left = 10;
  MYAPP.calcurator.right = 20;
  function sum(){
    return MYAPP.calculator.left + MYAPP.calcurator.right;
  }
  document.write(sum());
}()) <-//함수를 호출하는 부분
```

=> 함수를 바로 호출함으로써 하나의 전역변수도 사용하지 않음, 함수의 지역변수로 사용

### 유효범위의 대상(함수)

```javascript
// javascript

for(var i=0; i<1; i++){
  var name = 'coding everybody'
}
alert(name);

// 'coding everybody'
// java
for(int i=0; i<10; i++){
  String name = "egoing";
}
System.out.println(name);

// 출력결과 없음
```

=> **자바스크립트**에서는 for문 안에서 선언한 지역변수를 밖에서 호출해도 출력가능 (`{}` 중갈호 유효범위에 해당하지 않음)

​	* 자바스크립트만의 특징

=> **자바** 에서는 함수 뿐만 아니라 for문안에 지역변수를 밖에서 호출해도 호출이 되지않는다.

### 정적 유효범위(Static), Lexical 유효범위

```javascript
var i = 5;

function a(){
  var i = 10;
  b();
}

function b(){
  document.write(i);
}
a()

// 5
```

=> 여기서 핵심은 `function b()` 에서 지역변수 `i` 가 어디에 전역변수를 쓸 것이냐가 쟁점인데, `function a()` 의 `i`가 아닌 가장 바깥의 전역변수 `i` 의 값을 출력하게 된다. 즉, `function b()` 의 전역변수는 **함수 호출시점인 아닌 함수 정의 시점에서의 지역변수를 가져온다.**

- 반대로 호출되는 시점에서 바로 상위 전역변수에 접근이 가능하다면 그것은 **동적 유효범위**에 해당한다.



##### **7/26**(금)

#### 값으로서의 함수와 콜백

* 리턴값으로의 함수의 사용

```javascript
function cal(mode){
    var funcs = {
        'plus' : function(left, right){return left + right},
      	'minus' : function(left, right){return left - right}
    }
    return funcs[mode];
}

alert(cal('plus')(2,1));
// 3
```

=> `cal('plus')` 를 호출하게 되면 `cal` 함수 인자값에 `'plus'`  가 들어가게 되고,

​	`funcs['plus']`를 리턴하게 된다.

​	`funcs['plus']` 의 value값인 `function(left, right){return left + right}` 함수가 실행된다.

​	결국 `cal('plus')` 는 `function(left, right){return left + right}` 과 동일하다.

​	다음으로, 소괄호는 함수의 실행을 의미함으로 함수 인자값으로 `(2,1)` 넣음으로써 결과값은 `3`이 된다.



* 배열로서의 함수의 사용

```javascript
var process = [
    function(input){ return input + 10;},
    function(input){ return input * input;},
    function(input){ return input / 2;}
];
var input = 1;
for(var i = 0; i < process.length; i++){
    input = process[i](input);
}
alert(input);
```



**7/28(일)**

### 값으로서의 함수와 콜백 - 콜백이란?

### 처리의 위임

=> 값으로 사용될 수 있는 특성을 이용하면 함수의 인자로 함수를 전달할 수 있다. 값으로 전달된 함수는 호출될 수 있기 때문에 이를 이용하면 함수의 동작을 완전히 바꿀 수 있다. 인자로 전달된 함수 sortNumber의 구현에 따라서 sort의 동작방법이 완전히 바뀌게 된다.

```javascript
function sortNumber(a,b){
  return b-a; // 역순
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
alert(numbers.sort(sortNumber)); // array, [20,10,9,8,7,6,5,4,3,2,1]

function sortNumber(a,b){
  return a-b; // 정렬
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
alert(numbers.sort(sortNumber)); // array, [1,2,3,4,5,6,7,8,9,10,20]
```

=> sortNumber 함수를 콜백함수라고 부른다.

Sort() 내장함수에는 기본적으로 비교하여 정렬을 하는 알고리즘이 구현되어 있다.

콜백함수로 두개의 비교값을 넣어서 비교하게되면 자체적으로 두 수의 차이가 음수인지 양수인지 0인지를 비교하여 정렬하게 된다.



**8/1(목)**

### 비동기 처리

콜백은 비동기처리에서도 유용함. 시간이 오래 걸리는 작업이 있을 때 이 작업이 완료된 후에 처리해야 할 일을 콜백으로 지정하면 해당 작업이 끝났을 때 미리 등록한 작업을 실행하도록 할 수 있다.



#### 동기적(Synchronous)

=> 글작성 -> 이메일 발송 -> 작성완료(순차적으로 진행)

(앞에 작업이 다 끝나야 다음 작업을 실행)

예를 들어 웹창에서 어떠한 창을 클릭한 순간 다음 작업이 다 수행되기 전까지는 홈페이지가 freezing된다. 

#### 비동기적(Asynchronous)

=> 글작성 -> 이메일 발송 예약 -> 작성완료

(이메일 발송 예약 작업이 들어왔다면 일을 처리. 현재 다 못하는 걸 다른데 잠시 기록해놓고 급하넉 부터 처리)

```javascript
// datasourece.json.js
{ "title": "JavaScript", "author":"egoing"}

// 0801_sync_async.html

<!DOCTYPE html>
<html>
<head>
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
<script type="text/javascript">
    $.get('./datasource.json.js', function(result){
        console.log(result);
    }, 'json');
</script>
</body>
</html>
```

=> `$.get()` 으로 `datasource.json.js` 파일을 가져와서 그 객체를 콜백함수 인자값 `result`에 담아서 `json` 형태로 출력



### 클로저(Closure)

* 클로저(closure)는 내부함수가 외부함수의 맥락(context)에 접근할 수 있는 것을 가르킨다. 클로저는 자바스크립트를 이용한 고난이도의 테크닉을 구사하는데 필수적인 개념으로 활용된다.



#### 내부함수

* 자바스크립트는 함수 안에서 또 다른 함수를 선언할 수 있다. 아래의 예제를 보자. 결과는 경고창에 coding everybody가 출력될 것이다.

```javascript
function outter(){
  function inner(){
    var title = 'coding everybody';
    alert(title);
  }
  inner();
}
outter();
```

=> 함수 `outer` 내부에는 함수`inner` 가 정의되어 있는데 이 것을 내부 함수라고 한다.

내부함수는 **외부함수의 지역변수에 접근 할 수 있다**. 아래의 예제를 보자.

```javascript
function outter(){
      var title = 'coding';
  function inner(){
    alert(title);
  }
  inner();
}
outter();
//coding
```



#### 클로저

* 클로저(closure)는 내부함수와 밀접한 관계를 가지고 있는 주제다. 내부함수는 외부함수의 지역변수에 접근 할 수 있는데 외부함수의 실행이 끝나서 외부함수가 소멸된 이후에도 내부함수가 외부함수의 변수에 접근 할 수 있다.

```javascript
<script>
    function outter() {
    var title = 'coding everybody';
    return function(){
      alert(title);
    }
  }
    inner = outter();
    inner();
</script>
// coding everybody
```



### Private variable

* 소프트웨어가 커지는 과정에서 어떠한 정보가 있을 때 그 정보를 아무나 수정못하게 방지하는 것.

```javascript
<script>
        function factory_movie(title){
            return {
                get_title : function (){
                    return title;
                },
                set_title : function(_title){
                    title = _title
                }
            }
        }
        ghost = factory_movie('Ghost in the shell');
        matrix = factory_movie('Matrix');

        alert(ghost.get_title()); // 'Ghost in the shell'
        alert(matrix.get_title()); // 'Matrix'

        ghost.set_title('공각기동대');

        alert(ghost.get_title()); //'공각기동대'
        alert(matrix.get_title()); //'Matrix'
    </script>
```



**8/6(화)**

### arguments

함수에는 argumets라는 변수에 담긴 숨겨진 유사 배열이 있다. 이 배열에는 함수를 호출할 때 입력한 인자가 담겨있다.

```	javascript
function sum() {
  var i, _sum = 0;
  for (i = 0; i < arguments.length; i++) {
    document.write(i + ' : ' + arguments[i] + '<br />');
    _sum += arguments[i];
  }
  return _sum;
}
document.write('result : ' + sum(1, 2, 3, 4));

```

=> `arguments` 는 javascript에서 약속된 인자값. `sum(1,2,3,4)` 에서 인자값이 배열로 들어가는 것이 arguments다.

위 코드에서는 for문을 통해 인자값으로 들어온 배열에서 인덱스 별로 어떤값이 들어있는지 알 수 있다.



### 매개변수의 수

```javascript
function zero(){
  console.log(
    'zero.length', zero.length,
    'arguments', arguments.length
  );
}
function one(arg1){
  console.log(
    'one.length', one.length,
    'arguments', arguments.length
  );
}
function two(arg1, arg2){
  console.log(
    'two.length', two.length,
    'arguments', arguments.length
  );
}
zero(); // zero.length 0 arguments 0 
one('val1', 'val2');  // one.length 1 arguments 2 
two('val1');  // two.length 2 arguments 1
```

`함수명.length` 는 **정의된 함수의 인자값**의 수를 반환

`arguments.length` 는 **함수 호출 시 인자값**의 수를 반환

=> 함수 정의할때 인자값을 정해주면 정해진 수만큼 호출시에 인자값을 넘겨줘야함.

만약 이 둘의 값이 다르면 에러를 발생시킬때 유용



### **apply**(), call()

```javascript
 function sum(arg1,arg2){
            return arg1+arg2
        }
				alert(sum(1,2))
				// 3
        alert(sum.apply(null,[1,2]));
        a = [3,2]

				sum.apply
			
```

`sum(arg1,arg2)` 는 function(함수)의 객체이다. 그러므로 기본적으로 function을 상속받으므로 내장함수인 `apply()` 를 호출할 수 있다.

```javascript
o1 = { val1: 1, val2: 2, val3: 3 }
o2 = { v1: 10, v2: 50, v3: 100, v4: 25 }
function sum() {
  var _sum = 0;
  for (name in this) {
    _sum += this[name];
  }
  return _sum;
}
alert(sum.apply(o1)) // 6
alert(sum.apply(o2)) // 185

// o1.sum
// 02.sum
```

=> `apply()`는 인자값을 배열로, `call()`은 인자값 각각을 넘겨줌으로써 `this` 를 사용하면 함수내에서 값을 사용할 수도 변경할 수도 있다.