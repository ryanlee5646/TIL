# DAY09

## Web

------

- 고객(요청하는 컴퓨터, client, ex)Chrome ) 은 요청(request)하고 해주는 사람(server)은 요청을 처리해주고 한장의 문서로 response를 돌려준다.
- 서버는 다수의 클라이언트의 요청을 처리 해야 하기 때문에 다수의 컴퓨터로 처리한다.
- 요청의 종류
  - Get(받다): 주세요. 서버로 부터 HTML문서를 받는다.
  - Post(보내다): 처리해주세요. 데이터베이스에 저장, 연산을 요청하고 결과를 받음 등
- 우리는 서버 컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.

### Static Web (정말 단순한 웹 서비스)

- 변형, 연산이 없는 웹 서비스
- 요청을 보내는 게 브라우저의 기본 역할이다.
- 브라우저로 IP를 통해서 남의 컴퓨터로 접근 할 수도 있다.

### Dynamic Web

- Web Application program (Web APP)
- 같은 문서라고 해도 요청한 사람, 지역마다 다른 페이지, 다른 연산을 보여주게 된다.

##### 모든 서비스에서 요청을 하는 방법

- 브라우저 주소창에다가 주소(URI)를 입력한다.
- URL(Uniform Resource Locater)은 네트워크 상에서 자원이 어디 있는지를 알려주기 위한 고유 규약이다. URL은 웹 사이트 주소뿐만 아니라 컴퓨터 네트워크상의 모든 자원을 나타낼 수 있다.
- URI(Uniform Resource Identifier)는 자원 식별자로 요청하는 주소를 파일이라기 보다 구분자로 보는 것이다.
- 현재는 위치(locater) 보다는 식벽자(identifier)로 서비스를 요청한다.

## HTML(Hyper Text Markup Language)

- HTTP(Hyper Text Transfer Protocol)
- Hyper Text: 비 성형적으로 이루어진 텍스트. 기본적으로 Hyper Link를 통해 텍스트를 이동한다.
- HTML은 구문을 구분해서 글자의 크기를 변경하거나 꾸미는 기능을 한다.
- 컴퓨터는 HTML 요소로 쓰여진 raw text를 해석한다
- html 새 파일 생성
  - `html:5` `tap`을 하면 자동으로 html 틀이 완성된다.
- head, body 등도 `h, b`하고 `tap`을 하면 자동 완성 된다.

#### 요소(Element)

- HTML의 element는 태그와 내용(contents)로 구성되어 있다.
- 태그는 대소문자를 구별하지 않으나 소문자로 작성해야 한다. 요소간의 중첩도 가능하다.
- 닫는 태그가 없는 태그도 존재한다.
  - `img src="url"/>`

#### 속성(Attribute)

- 태그에는 속성이 지정될 수 있다.
- `<a href="https://google.com"/>`= 앞뒤로 띄워쓰기 안하고 큰따옴표 사용이 표준
- 구글로 이동하는 버튼이 생성됨
- hyper referecne

#### DOM 트리

- 태그는 중첩되어 사용가능하며, 이때 다음과 같은 관계를 갖는다.

```
<body>
	<h1>웹문서</h1>   body와 h1은 부모자식
	<ul>
		<li>HTML</li> li는 형제관계
		<li>CSS</li> ui와 li는 형제관계
    </ul>
    </h1
</body>
```

#### 시맨틱 태그

- 컨텐츠의 의미를 설명하는 태그로서, HTML5에 새롭게 추가된 시맨틱 태그가 있다.
- header: 헤더(문서 전체나 섹션의 헤더)
- nav: 내비게이션
- aside: 사이드에 위치한 공간으로, 메인 컨텐츠와 관련성이 적은 컨텐츠에 사용
- section: 문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 h1~h6요소를 가짐
- article: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역(포럼/신문의 글 기사)
- footer: 푸터(문서 전체나 섹션의 푸터)
- Chrome web store에서 Web developer 설치, information-view document outline

### Web Practice

- section에 id값을 지정하고, 파이썬과 웹을 누르면 각각의 항목으로 이동하도록 해봅시다.
- 참고사이트는 같은 폴더 내에 있는 index.html 파일로 이동하도록 해봅시다.
- 공간을 만들때 사용

#### 동영상 embed

- Youtbe-[공유]-[퍼가기] <iframe> 내용 복사 붙여넣기

#### Table

- 전체는 Table
- 첫 row줄은 t head로 쓰인다
- 행은 tr, 열은 td
- table>tr*3: 한번에 tr 3줄이 만들어진다.
- 초밥: 초밥을 가로2칸으로 늘린다.
- 짬뽕: 짬뽕을 세로 2칸으로 늘린다
- *span을 사용할 때는 늘려지는 부분에 td, tr, th 같은 선언이 없어야 한다.
  - 3칸 쓰는데 1칸 침범당했다면 2칸만 선언및 정의해야 한다.

# DAY10

## CSS

- cascading style Sheets
- HTML은 구조만 하고 CSS가 styling을 한다.
- CSS를 잘못작성해도 웹은 작동된다.
- HTML문서안의 <style>에 작성할 수 있다.
  - 주석:` /* */`

```
<style>
        /* CSS */
        /* h1 : 선택자 */
        /* color : 속성 (Property) */
        /* aqua : 값 (Value) */
        /* { } : 선언 블록 */
        /* color: aqua; : 선언문 */
        /* 전체 : 규칙 (Rule) */
        /* 규칙 묶음 : 스타일 시트 (Style Sheet) */
        h1 {
            color: aqua;
        }
    </style>
```

#### style 작성 방법 3가지

1. Inliine style

```
<!
<!-- 1. Inliine style (인라인 스타일) -->
        <ul style="list-style-type: circle;">
```

- 인라인 스타일은 선택자가 필요없다. 태그 안에서 바로 스타일을 적용하기 때문에

1. Embedding style

```
<!-- 2. Embedding style (style tage 사용하기) -->
<style>
        /* CSS */
        /* h1 : 선택자 */
        /* color : 속성 (Property) */
        /* aqua : 값 (Value) */
        h1 {
            color: aqua;
        }
    </style>
```

- HTML문서 내에 포함되어 있다

1. Link style (css 파일 link)

```
/* style.css */
h3{
    color: aquq;
}
<!-- index.html -->
<!-- 3. Link style (css 파일 link) -->
    <link rel="stylesheet" href="style.css">
```

#### 선택자

- 전체선택자
  - 모든 선택자에 속성과 값을 지정한다.
  - default로 하고 싶은 값을 전체선택자로 설정한다.

```
<style>
	* {
        color: red;
	}
</style>
```

- 태그 선택자
  - 해당 선택자의 태그에 속성과 값을 지정할 수 있다.

```
 /* 태그 선택자 */
        h1 {
            color: rosybrown;
        }
```

- 클래스 선택자
  - 해당 클래스(모임)에 속성과 값을 지정할 수 있다.

```
 /* 클래스 선택자 */
        .blue {
            color: blue;
        }
<h2 class="blue">blue, .클래스 선택자</h2>
```

- ID 선택자
  - 선택자가 가진 고유 값으로 속성과 값을 지정할 수 있다.

```
 /* 아이디 선택자 */
        #green {
            color: green;
        }
<h3 id="green">green, #아이디 선택자</h3>
```

- 선택자의 우선순위

  아이디 > 클래스 > 태그 > *

#### 글자마다 style 적용

- span으로 감싸주고 style을 적용한다

```
<p>나는 <span class="blue">파랑색</span>이고 싶고,
여기는 <span class="pink">핑크색</span>이고 싶을 때는?</p>
```

#### color style

- color name

```
/* 1. color name */
        h1 {
            color: red;
        }
```

- RGB color code

```
h2 {
            /* RGB color code */
            color: #0000ff; 
        }
```

- rgb()

```
/* 3. rgb() */
        h3 {
            color: rgb(0, 255, 0)
        }
```

- rgba() 마지막 인수에 투명도 포함

```
 /* 4.rgba() */
        p {
            color: rgba(255, 0, 0, 0.3) /* alpha : 0.0 ~ 1.0 */     
        }
```

#### 단위길이 font size

```
/* font-size, 단위 길이 */
        html {
                font-size: 10px;
            }
        /* rem : html에 정의된 front-size에 비례 */
        ol {
            font-size: 1.2rem;
            /* 10px * 1.2 = 12px */
        }
        /* em : 자신의 상위 요소의 front-size에 비례 */
        ul {
            font-size: 1.2em;
        }
        .em {
            font-size: 1.2em;
        }
        /* 10px(html)  * 1.2(ul) * 1.2(li) =  14.4px */

        /* vh - view height, vw = view width */
        /* 사용자가 보고 있는 브라우저의 세로, 가로 길이 */
        .vh {
            font-size: 5vh;
        }
        .vw {
            font-size: 5vw;
        }
```

- px: 픽셀(절대값으로 보통 사용)
- rem: html에 정의된 front-size에 비례한 배수 크기로 font-size를 설정
  - ex) 10px * 1.2 = 12px
- em: 자신의 상위 요소의 front-size에 비례
  - ex) 10px(html) * 1.2(ul) * 1.2(li) = 14.4.px
- vh, vw: 사용자가 보고 있는 브라우저에 비례해서 세로, 가로 길이를 조절
  - vh: 브라우저에 비례해서 height 변경됨
  - vw: 브라우저에 비례해서 width 변경됨

#### box

##### box-sizing

box의 가로, 세로 크기를 지정 할 때 기준을 정할 수 있다

- border-box, content-box, ..

###### inline

inline 을 사용하면 줄 사이의 특정한 부분만 속성을 적용할 수 있다.

##### box 속성

- diplay: inline(컨텐츠에 맞춰서 박스가 표시됨), none(화면에 안보임)
- border: 보더 두께 선 색상 설정
- background-color: 배경색
- visibility: visible(기본값), hidden(박스가 안보임)
- opacity: 희미해짐 0.0~1.0

```
<style>
        /* 가로, 세로 */
        /* box */
        /* margin -> padding -> box로 갈수록 안쪽이다. */
        .box {
            width: 100px;
            height: 100px;
            /* padding: 25px; */
            padding-top: 25px;
            padding-bottom: 25px;
            padding-left: 25px;
            padding-right: 25px;
            margin: 25px;
            
            /* 테두리 */
            border: 2px solid purple;
            /* border */
            /* border-width: 2px; */
            /* 테두리 선 스타일 (실선, 점선 ,,) */
            /* border-style: solid;  */
            /* 테두리 선 색상 */
            /* border-color: purple;   */
            /* 둥근 모서리 */
            border-radius: 20px;
            /* box-sizing: content-box; */
            box-sizing: border-box;
        }
        /* 1. block */
        /* div, h1~h6, p, ol, ul, li, table, form */
        
        /* 2. inline */
        /* span, a, strong, em, img, input */
        /* width, height */
        /* margin-top, margin-bottom 사용 불가 */
        
        /* 3. inline-block */
        /* inline + block 특징 섞어서 가지고 있음 */
        
        /* 4. none */
        /* 화면에 보이지 않음. (공간조차 사라짐 */
        .box2 {
            display: inline;
            border: 2px solid red;
            background-color:  gray;
            /* visibility: hidden; */
            opacity: 0.2;
        }
        /* visibility: visible; (기본값) */
    </style>
```

##### box position

box-static

- 기본 위치값을 가지고 있고 세로, 가로 길이로 박스크기를 변경할 수 있다.

box-absolute

- 페이지 시작 화면(0, 0)을 기준점으로 해서 top, left 등의 값을 변경시켜서 박스의 시작점을 옮길 수 있다.
- 상위 계층이 있으면 상위 박스의 위치를 기준으로 박스 위치가 정해진다.

box-relative

- 다른 박스와의 상대적으로 거리로 박스의 위치가 지정된다.
- 박스의 원래 위치가 기준이 되고, 그 기준 위치의 상대위치로 박스 position이 결정된다.

box-fixed

- 현재 보이는 페이지 화면을 기준점으로 해서 박스를 위치시킨다.
- 항상 페이지에 고정되어 있음

z-index

- 박스의 z-index 값이 다른 박스의 z-index보다 크면 박스가 다른 박스 앞에 위치된다.
- 박스들이 겹칠때 앞으로 오게하거나 맨 뒤로 보내거나 하는 용도로 쓸 수 있다.
- static은 다른 박스와 상호작용을 못하기 때문에 z-index가 안먹힘

```
<body>
    <div class="box-static">
        static
    </div>
    <div class="box-absolute">
        absolute
    </div>
    <div class="box-relative">
        relative
    </div>
    <div class="box-fixed">
        fixed
    </div>
</body>
/* 기본값 위치 static */
.box-static {
    background-color: gray;
    border: 2px solid red;
    width: 100px;
    height: 100px;
}
/* 2.absolute */
.box-absolute {
    position: absolute;
    background: green;
    width: 100px;
    height: 100px;
    /* 화면 (0,0) 기준으로 이동 */
    top: 50px;
    left: 50px;
    z-index: 1;
}

/* 3. relative */
.box-relative {
    position: relative;
    background: blue;
    width: 100px;
    height: 100px;
    z-index: 2;
}

/* 4. fixed */
.box-fixed {
    position: fixed;
    background-color: pink;
    width: 100px;
    height: 100px;
    top: 50px;
    right: 50px;
}
```

#### Background

- background-size: cover
  - 큰 쪽으로 사진의 비율을 맞춘다
- background-size: contain;
  - 작은 쪽으로 사진의 비율을 맞춘다.
- background-repeat: no-repeat
  - 사진을 여러개 반복하지 않고 하나만 나타낸다
- background-attachment: fixed
  - 스크롤을 내려도 배경이 고정된다.

```
.background-color {
    background-color: blue;

}
.background-image {
    background-image : url(images/python.png);
    background-position: center center;
    /* background-size: 200px 200px; */
    background-size: contain;
    background-repeat: no-repeat;
    background-attachment: fixed
}
```

#### Font

```
.font { 
    font-size: 40px;
    font-style: italic;
    font-weight: 700; /* == bold */
    font-family: 'Times New Roman', Times, serif
}
```

- font-weight: 두께 조절

font-family는 첫번째 인수의 폰트가 없으면 다음 인수 폰트로 넘어가서 적용한다.

보통 safe font-family를 적용해 모든 웹에서 폰트를 찾아 적용할 수 있도록 해준다.

- line_height: font-size의 배수
- letter-spacing: 장평
- text-alling: 글의 위치 설정 (가운데 맞춤 등)

# D11

#### 선택자

정확한 속성 값을 입력하지 않아도 찾을 수 있는 선택자

이미지를 alt 값을 통해 접근을 할 때 또는 태그를 속성으로 접근 할 때 사용한다.

정확한 값을 입력안해도 찾을 수 있는 선택자

 1. [속성="값"]

 2. [속성~="값"] : alt="바다 사진" / [alt~="바다]

 alt에 "바다 사진"이라고 되어 있을때 속성~="값"을 하면 '바다 사진'을 찾을수 있다.

 3. [속성|="값"] : alt="바다-사진" / [alt|="바다"]

 4. [속성^="값"] : alt="apple banana" / [alt^="app"]

 5. [속성$="값"] : href="ssafy.com/istj" / [href$="istj"]

 6. [속성*="값"] : alt="미세먼지싫어" / [alt*="세먼지"]

Chrome - 확장프로그램- Wappalyzer 설치

페이지에 사용된 framework를 볼 수 있다.