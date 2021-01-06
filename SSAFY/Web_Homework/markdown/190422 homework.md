1. **JS는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5까지는 ‘var‘ 키워드로 변수를 선언했다면, ES6 이후로는 ‘let’과 ‘const’ 키워드가 등장했다. ‘let’과 ‘const’의 차이점과 언제 사용하는지 간략하게 기술하시오.**

* `let` : 재할당 가능, 주로 반복문, 변수 같은 경우 
* `const`: 재할당 불가능, 함수 선언할때? (의도치 않은 할당을 막을 수 있다.)

2. **JS에서는 key –value로 이루어진 자료구조를 Object라고 부른다. Object와 JSON의 차이를 간략하게 기술하시오.**

* **Object**: js engine 메모리 안에 있는 데이터 구조(자바스크립트의 자료형)
* **JSON** : 객체의 내용을 기술하기 위한 text 파일이라는 점이 다르다.(데이터 구조를 표현한 단순한 문자열)

3. **해당코드에서 ‘Value’에 접근하는 두 가지 방법(코드)을 모두 작성하시오.**

```js
const myobject = {
    key:'Value'
}
```

```js
myobject['key']
myobject.key
```



4. **아래 주석에 따라 JS코드를 작성하시오.**

```html
<!DOCTYPE html> 
<html lang="en"> 
<head>
<title>Document</title> 
</head> 
<body> 
<h1>Hello World!</h1> 
<script>
// 1. h1 태그를 선택한 뒤, header 라는 상수에 할당한다.
    let header = document.querySelector('h1')
    
// 2. 브라우저 콘솔에 header 안의 내용을 출력한다.
    console.log(header.innerText)
    
// 3. header 안의 내용을 'Happy Hacking!' 으로 변경한다. 
    header.innerText = 'Happy Hacking!'
</script> 
</body> 
</html>
```

