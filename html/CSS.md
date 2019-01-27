# CSS

**CSS(Cascading Stype Sheets):** 마크업 언어(HTML)이 실제 표시되는 방법을 기술하는 언어.

**HTML**이 웹사이트의 몸체를 담당한다면, CSS는 옷, 엑세서리와 같이 웹사이트를 꾸미는 역할을 담당한다.

CSS를 잘못 작성해도 웹은 작동한다.

- **Bootstrap:** 트위터를 만든 회사에서 만든 CSS Framework를 제공하는 사이트 (<http://bootstrapk.com/>)
- **CSS Framework**를 활용하면, HTML의 스타일을 직접 하지 않고, 적절한 디자인을 적용할 수 있음. (HTML Style을 도와주는 서비스 혹은 라이브러리의 개념)

> 웹 표준은 이제 더 이상 무시할 수 없는 키워드입니다.
>
> World Wide Web(WWW)의 의미대로 가능한 많은 사람이 웹을 이용하기 위해서는, 모든 브라우저에서 ‘똑같이 보이는 것’이 아니라 ‘각 브라우저에 알맞게 보이는 것’이 중요하기 때문입니다.
>
> 그래서 웹 표준에서는 구조(Constructure)와 표현(Presentation)과 행위(Behavior)를 각각 분리해서 개발하기를 권유합니다.
>
> 이렇게 하면, 각 사용자는 구조화 된 마크업에 따라 다양한 디자인을 제공받을 수 있기 때문입니다. 뿐만 아니라 사이트의 로딩속도도 빨라지고 개발과 유지보수 또한 쉬워집니다.
>
> - 구조 : 웹 콘텐츠에 의미를 부여하고 구조를 형성 → HTML
> - 표현 : 시각적인 디자인과 레이아웃 표현 → CSS
> - 행위 : 모든 front-end의 브라우저 상호작용을 담당 → JavaScript
>
> ​	참조: <http://www.nextree.co.kr/p8468/>

### CSS 기본 구성

```css
<!DOCTYPE html>
<html lang="en">
    <head>
		<style>
            h1 {
                color: aqua;
        </style>
    </head>
```

- `h1` : 선택자
- `color` : 속성(property)
- `aqua` : 값(value)
- `{}` : 선언 블록
- `color: aqua;` : 선언문
- `h1(선택자) + {color: red;}(선언블록)` : 규칙(Rule)
- `규칙 묶음` : 스타일 시트(stylesheet)



### CSS 스타일의 종류

**1) Inline style (인라인 스타일)**

```html
<body>
	<section id="web">
        <ul style="list-style-type: circle;">
            <li>HTML</li>
            <li>CSS</li>
        </ul>
    </section>
</body>
```

* 인라인 스타일은 태그 안에서 바로 스타일을 적용하기 때문에 선택자가 필요없다. 

**2) Embedding style (style tag 사용하기)**

```html
<head>
    <style>
        h1 {
            color: red;
    </style>
</head>
```

**3) Link style (css 파일 link)**

```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```



### 선택자 (Selector)

------

선택자란 말 그대로 선택을 해주는 요소를 말함. 이를 통해 특정 요소들을 선택하여 스타일을 적용 할 수 있게 됨.

**1) 전체 선택자**

- 선택자에 `*` 을 사용 할 경우, head 및 body 안의 모든 내용에 스타일이 적용 됨.

```
<head>
    <style>
        * {
            color: red;
        }
    </style>
</head>
<body>
    <p>Red, 전체 선택자</p>
</body>
```

**2) 태그 선택자**

- 스타일을 적용하고 싶은 태그명을 선택자에 입력하면, 그 태그에만 스타일이 적용됨.

```
<head>
    <style>
        h1 {
            color: rosybrown;
        }
    </style>
</head>
<body>
    <h1>rosybrown, 태그 선택자</h1>
</body>
```

**3) 클래스 선택자**

- 사용자가 지정한 클래스에 대하여 스타일을 적용함.
- 클래스를 `class="blue"` 와 같이 적용하고자 하는 태그에 클래스를 지정.
- 선택자에는 `.blue` 와 같이, `.` 을 클래스 앞에 반드시 입력해줘야 함.

```
<head>
    <style>
        .blue {
            color: blue;
        }
    </style>
</head>
<body>
    <h2 class="blue">blue, .클래스 선택자</h2>
</body>
```

**4) 아이디 선택자**

- 사용자가 지정한 아이디에 대하여 스타일을 적용함.
- 아이디는 html문서안에 유일하게 하나만 가질 수 있음.
- 아이디를 `id="green"` 와 같이, 적용하고자 하는 태그에 아이디를 지정.
- 선택자에는 `#green` 와 같이, `#` 을 아이디 앞에 반드시 입력해줘야 함.

```
<head>
    <style>
        #green {
            color: green;
        }
    </style>
</head>
<body>
    <h3 id="green">green, #아이디 선택자</h3>
</body>
```

#### 복합 선택자

**1) 자손 선택자**

- 모든 자손들이 선택됨.
- 아래의 경우, section 태그 안에 있는 모든 ul 태그에 속성이 적용됨.

```
section ul {
    margin: 10px 0;}
```

**2) 자식 선택자**

- 지정된 자식에게만 속성이 적용됨

```
section > ul > li {
    font-size: 20px;
    font-weight: bold;
}
```

**3) 형제 선택자**

- `a + ul `: 같은 부모 내, a의 형제 요소 중 바로 뒤 (다음)의 ul에 적용
- `a ~ ul` : a의 형제 요소 중, a 뒤에 오는 모든 ul에 적용

```
a + ul {
    background-color: gold;}
a ~ ul {
    border:  1px solid darkgray;}
```

**4) 속성 선택자**

- class라는 속성을 가진 ul 태그 중, li 라는 자손 모두에 적용

```
ul[class] li {
    width: 24%;
    height: 50px;
    display: inline-block;
}
```

- target 속성을 가지며, 그 값이 _self인 a태그에 적용

```
a[target="_self"] {
    border: 1px solid darkgray;
    border-radius: 5px;
    background-color: white;
    padding: 5px;
}
```

- [속성="값"]
- [속성~="값"]
  - alt="바다 사진" / [alt~="바다"]
- [속성|="값"]
  - alt="바다-사진" / [alt|="바다"]
- [속성^="값"] : 시작하는 값 찾기
  - alt="apple banana" / [alt^="app"]
- [속성$="값"] : 끝나는 값 찾기
  - href="ssafy.com/istj" / [href$="istj"]
- [속성*="값"] : 특정 값만포함하면 선택
  - alt="미세먼지싫어" / [alt*="세먼지"]

#### 선택자의 우선순위

- 태그 vs 클래스: 클래스 선택자 우선
- 태그 vs 아이디: 아이디 선택자 우선
- 태그 vs 아이디 vs 클래스: 아이디 선택자 우선
- 최종 우선 순위: 아이디 > 클래스 > 태그 > 전체 (요소들의 갯수 순서대로 라고 볼 수 있음)

```
<body>
    <!-- vs. -->
    <!-- id > class > tag > *  -->
    
    <!-- 태그 vs 클래스: 클래스 -->
    <h1 class="blue">h1 vs .blue</h1>
    
    <!-- 태그 vs 아이디: 아이디 -->
    <h1 id="green">h1 vs #green</h1>
    
    <!-- 태그 vs 아이디 vs 클래스: 아이디 -->
    <h1 id="green" class="blue">h1 vs #green vs class</h1>
    
</body>
```

**1/17일자 추가 정리 내용**

CSS의 선택자는 아래의 우선순위를 가짐.

```html
<body>
    <div>
        <h1 id="toffee" class="latte" style="color: green;">아이스 토피넛 라떼</h1>
    </div>
</body>
/* 우선순위가 낮은 것부터 적용 */

/* 6. 상위 객체에 의해 상속된 속성 */
div {color: red}
/* 5. 태그 이름으로 지정한 속성 */
h1 {color: blue;}
/* 4. 클래스 이름으로 지정한 속성 */
.latte {color: brown;}
/* 3. id로 지정한 속성 */
/* 동일한 레벨의 속성이 열거될 경우는 후자에 온 속성을 적용함 */
#toffee {color: yellow;}
#toffee {color: purple;}

/* 2. HTML에서 style을 직접 작성한 속성 */
/* 1. 속성값 뒤에 !important를 붙인 속성 */
h1 {color:black !important;}
```

**한 문장내 특정 부분에 각각 다른 스타일을 적용하고 싶을 때?**

- `span` 태그 이용

```
<body>
    <p>나는 <span class="blue">파랑색</span>이고 싶고, 
       여기는<span class="pink">핑크색</span>이고 싶을 때는?</p>
</body>
```



### CSS의 속성(Properties)

#### CSS Colors

**1) Color name**

**2) Color code**

**3) rgb**

**4) rgba**

- a(alpha)의 범위는 0.0~1.0 으로 값이 작아 질 수록, 색이 투명해짐.

```html
<head>
    <style>
        /* 1. color name */
        h1 {color: red;}
        
        /* 2. color code */
        h2 {color: #0000ff;}
        
        /* 3. rgb() */
        h3 {color: rgb(0,255,0);}
        
        /* 4. rgba() */
        /* 4. a(alpha): 0.0 ~ 1.0 */
        p {color: rgba(255,0,0,0.5)}   
    </style>
</head>
<body>
    <h1>빨간색</h1>
    <h2>파란색</h2>
    <h3>초록색</h3>
    <p>흐릿한 빨간색(투명도)</p>
</body>
```

#### CSS font-sizes

<https://www.w3schools.com/css/css_units.asp>

**1) 문서 전체의 단위 길이 적용**

```
<head>
    <style>
        /* 단위 길이(font-size) */
        html {font-size: 10px;}
</head>
```

**2) rem & em**

- 단위 길이를 다른 요소들과 비교하여 상대적으로 정함.

- ```
  rem
  ```

   

  : Root Element (html)의 폰트 사이즈가 기준이 됨.

  - 1.2 rem ; 10 px(html) * 1.2 = 12 px

- ```
  em
  ```

   

  : 상위 Element의 폰트 사이즈가 기준이 됨.

  - `<li class="em">저는 1.2em입니다.</li>` 에서, `li < ul < body < head` 순의 상위 Element 로 이동하여 기준 폰트사이즈 (html: 10px) 를 찾음.
  - 자손 선택자 `ul` & `li (Ul의 자식 선택자)`의 폰트 사이즈가 각각 `1.2 em`인 것을 알 수 있음.
  - 따라서, 최종적으로 10px(html) * 1.2(ul) * 1.2(ul안의 li) = 14.4 px

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        /* 단위 길이(font-size) */
        html {font-size: 10px;}
        
   		/* rem: html에 정의된 font-size에 비례 */
    	ol {font-size: 1.2rem;}
        /* 10px * 1.2 = 12px */
    
    	/* em: 자신의 상위 요소의 font-size에 비례 */
    	ul {font-size: 1.2em;}
    
        .em {font-size: 1.2em;}
        /* 10px(html) * 1.2(ul) * 1.2(ul li) = 14.4px */
     </style>
</head>

<body>
     <ol>
        <li>저는 1.2rem입니다.</li>
    </ol>
    <ul>
        <li class="em">저는 1.2em입니다.</li>
    </ul>  
</body>
```

**3) vh(viewpoint height) & vw(viewpoint height) **

- 사용자가 보고있는 브라우져의 세로,가로 길이 (상대적인 값)
- 브라우져의 크기를 의도적으로 수정할 경우, 폰트 사이즈의 크기가 자동으로 변경됨.

```html
<head>
    <style>
        .vh {font-size: 5vh;}
        .vw {font-size: 5vw;}
    </style>
</head>

<body>
    <span class="vh">5vh</span>
    <span class="vw">5vw</span>
</body>
```

#### CSS Box Model

모든 HTML 요소들은 박스로 간주 할 수 있으며, CSS Box Model은 문서의 design과 layout을 일컫음.

기본 구성 요소 (참조: <https://www.w3schools.com/css/css_boxmodel.asp>)

- Content
- Padding
- Margin
- Border

**1) box-sizing / width / height**

- ```
  box-sizing
  ```

   

  : 박스 크기의 기준을 설정할 수 있음. (기본:

   

  ```
  content-box
  ```

   

  )

  - 아래의 경우, 세로 & 가로 길이가 각각 100px 이며,
  - `box-sizing: border-box;` 인 경우, `border-box` 전체의 세로 가로 길이가 100px을 의미함.

- `width & height` : 박스의 너비 & 높이

```
<head>
    <style>
        box {
            box-sizing: content-box;
            width: 100px;
            height: 100px;
         }      
    </style>
</head>
```

**2) padding & margin**

- `padding` : border 의 안쪽 여백

- `margin` : border의 바깥쪽 여백

- `padding: 25px` 와 같이, 상/하/좌/우의 여백을 동시에 줄 수도 있으며,

  `padding-top: 25px` 와 같이, 개별적으로 여백을 적용 할 수 있다.

  cf) `padding: 25px 20px 15px 10px` 처럼, 연속적으로 각각의 여백을 한줄로 표현도 가능.

   순서는 위부터 시계 방향(위 / 오른쪽 / 아래 / 왼쪽)

```
<head>
    <style>
        box {
            /* 안쪽 여백 */
            /* padding: 25px */
            padding-top: 25px; 
            padding-right: 25px;
            padding-bottom: 25px;
            padding-left: 25px;
            /*margin: 25px 20px 15px 10px ; 바깥쪽 여백 */
            margin-top: 25px; 
            margin-right: 25px;
            margin-bottom: 25px;
            margin-left: 25px;
         }      
    </style>
</head>
```

**3) border**

- `border-width` : 테두리의 두께

- `border-style` : 테두리의 스타일

- `border-color` : 테두리 색상

  cf) `border: 2px solid purple;` 처럼 또한 연속적으로 테두리에 대한 설정을 할 수 있음.

   순서는 두께 > 스타일 > 색상 순임.

- `border-radius` : 테두리 모서리 둥글기 정도

```
<head>
    <style>
        box {
            
            /*border: 2px solid purple;*/            
            border-width: 2px;
            border-style: solid;
            border-color: purple;
            
            /* 테두리 모서리 둥글기 정도 */
            border-radius: 20px;            
         }      
    </style>
</head>
```

#### CSS Display

**1) Block-level Elements**

- 기본적으로 full width available 을 차지함. (전체 한 라인)
- 블록 레벨 속성은 항상 새로운 라인에서 시작함.
- 예) div, h1~h6, p, ol, ul, li, table, form

**2) Inline Elements**

- 자기자신을 담고 있는 곳 까지만 차지함(as much width as necessary)
- 인라인 속성은 새로운 라인에서 시작하지 않음.
- 예) span, a, strong, em, img, input
- *width, height, margin-top margin-bottom 사용 불가*

**3) Visibility & Opacity**

- Visibility: 박스를 보이게 하는 설정(기본값: visible)
- 값을 hidden으로 적용하면 박스를 안보이게 설정 할 수 있음
- Opacity: 박스의 투명도. 범위는 0.0~1.0으로 작아질수록 투명해짐

`div` 태그는 블록 레벨 속성을 갖고 있음. 따라서 컨텐츠 만큼만 디스플레이를 설정하기 위해서는 아래와 같이 `display: inline` 으로 의도적으로 변경을 해줘야 한다.

```
<head>
    <style>
        .box2 {
            display: inline;
            border: 2px solid red;
            background-color: gray;
            visibility: visible;
            opacity: 0.3;
        }
    </style>
</head>
<body>
    <div class="box2">
        이것은 박스 2 입니다.
    </div>
    
</body>
```

#### CSS Position

The position property specifies the type of positioning method used for an element (static, relative, fixed, absolute or sticky).

- Position: Static / absolute / relative / fixed

- top / bottom / left / right 속성을 이용하여 위치 수정 가능

  예) `top: 50px / left: 50px `: 테두리 내 기준으로 위에서 부터 50px,

   왼쪽에서 50px 이동

**각 박스의 위치가 겹치는 경우 z-index 속성을 이용하여 우선순위를 설정할 수 있음.* *static은 다른 박스와 상호작용을 못하기 때문에 z-index가 안먹힘*.

**1) Static (Default)**

- top / bottom / left/ right 속성등에 영향을 받지 않음
- 위치는 페이지의 일반적인 흐름에 따라 결정됨. (CSS Position의 기본값)

```
.box-static {
    background-color: gray;
    border: 2px solid red;
    width: 100px;
    height: 100px;}
```

**2) absolute**

- 좌표(절대값) 기준으로 화면 내 어디로든 자유롭게 이동 가능.
- 이동할 경우, 기존 위치는 아애 비워져버리므로. static box가 있는 경우, 순차적으로 그자리를 차지해버림. (본가가 이사간다!)

```
.box-absolute {
    position: absolute;
    background: green;
    width: 100px;
    height: 100px;
    top: 50px;
    left: 50px;
    z-index: 1;}
```

**3) relative**

- Normal position (기존 위치)를 기준으로 이동(상대적 이동)
- 이동하여도, Normal position은 다른 content에 의해 차지되지 않음.
- (본가는 그대로 있고, 자취방을 구한다는 개념!)

```
.box-relative {
    position: relative;
    background: blue;
    width: 100px;
    height: 100px;
    z-index:2;}
```

**4) fixed**

- 스크롤 바를 내려도 고정적으로 보이는 부분.
- 이동할 경우, 기존 위치는 아애 비워져버리므로. static box가 있는 경우, 순차적으로 그자리를 차지해버림. (본가가 이사간다!)

```
.box-fixed {
    position: fixed;
    background: pink;
    width: 100px;
    height: 100px;
    top: 50px;
    right: 50px;}
```

**5) 응용**

- position을 설정한 태그 안에 추가로 태그를 넣음으로써, 기준점(시작점)을 설정 할 수도 있음.

```
<body>
	<div class="small-box" id="green">
      <div class="small-box" id="purple"></div> 
        <!-- green 안에 purple -->
    </div>
    <div class="small-box" id="blue">
      <div class="small-box" id="orange"></div> 
        <!-- blue 안에 orange -->
	</div>
</body>

<-- .CSS file -->
<style>
#purple {
  background-color: purple;
  /* 초록색 기준으로 100 100 만큼 떨어져 있음 */
  position: absolute;
  top: 100px;
  left: 100px;
}

#orange {
  background: orange;
  /* 파란색 기준으로 얼마나 떨어져있는가 */
  position: absolute;
  top: -100px;
  left: 100px;
}
</style>
```

#### CSS background

CSS background의 속성은 속성에 대한 배경 효과를 설정하는데 사용한다.

The CSS background properties are used to define the background effects for elements.

- `background-color` : 배경 색상 설정

- `background-image `: 이미지 설정. 예) `url(images/minsu.jpg);`

- `background-position` : 가로 세로 초점 이동 설정

  예) `background-position: center center` 

- `background-size` : 배경의 크기 설정

  - 직접 수치 입력 (예. 200px 200px)
  - `contain` : 이미지가 완전히 보이도록 배경 이미지 크기 조정
  - `cover` : 전체 컨테이너를 덮을 수 있도록 배경 이미지 크기 조정

- `background-repeat` : 배경 이미지 반복 설정

  - no repeat: 반복하지 않음. (이미지는 1번만 표시)
  - repeat: 가로/세로로 반복. 적합하지 않을 시, 마지막 이미지가 잘림.
  - initial: 속성을 기본값으로 설정

- `background-attachment` : 배경 이미지 고정 / 스크롤 여부 설정

  - scroll: 배경이미지가 페이지와 함께 스크롤됨 (기본값)
  - fixed: 배경이미지가 페이지와 함께 스크롤 되지 않음

```
div {
    height: 200px;
}

.background-color {
    background-color: blue;
}
.background-image {
    background-image: url(images/minsu.jpg);
    /* 가로,세로 초점 이동 */
    /*(left, right, top, bottom, center)*/
    background-position: center center; 
    /* contain & 200px 200px & cover */
    background-size: cover;
    background-repeat: no-repeat;
    /* fixed & scroll */
    background-attachment: fixed;
}
```

#### CSS font

- `font-size` : font의 크기 설정
- `font-style` : font의 스타일 설정
- `font-weight`: font의 굵음의 정도 설정 (일반적으로 100~900 사이)
- `font-family` : font 종류를 지정
  - 컴퓨터에 모든 폰트가 들어 있지 않으므로, font-name 중 원하는 폰트를 여러가지 나열하여, (font-stack) 마지막에 generic-family를 적어줌.
  - 이를 통해, 적어도 폰트가 없을 때, 끝에 있는 generic fa,ily에서비슷한 폰트를 브라우저가 찾아서 보여줌.
  - web-safe font 종류: verdana / georgia / times new roman / aria
  - 구글 폰트( `https://fonts.google.com/` )를 통해서 다양한 폰트를 적용 할 수도 있음.
- `line-height` : 줄 간격 설정
  - font 사이즈에 비례하여 상대적으로 설정하거나 (기준: font size 1),
  - 픽셀 크기로 설정 가능
- `letter-spacing` : font의 장평 조절 (플러스로 가면, 장평이커지고 마이너스로 가면 장평이작아짐)
- `text-align` : 정렬 위치 설정 (center, end, inherit)

```html
.font {
    font-size: 40px;
    font-style: italic;
    font-weight: 700;
    font-family: 'Times New Roman', Times, serif
    line-height: 1.5;
    letter-spacing: 1px;
    text-align: center;
}
```

# Responsive Web

반응형 웹: **반응형 웹 디자인**(responsive web design, RWD)이란 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 [디스플레이](https://ko.wikipedia.org/wiki/%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4)의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법을 말한다.

CSS 및 HTML을 사용하여 내용을 조정, 숨기기, 축소, 확대 또는 이동하여 화면에서 보기 좋게 만드는 형식

### View port

view port는 가로 해상도를 의미하며, 웹페이지의 사용자가 볼 수 있는 영역을 말함.

여태껏 우리는 VS CODE 자동 완성 기능을 통해 view port를 meta tag로서 head 요소 안에 넣어 놓고 진행 해옴.

```
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

뷰포트는 모바일기기에 화면이 로드 되었을 때, 페이지가 적정 해상도로 로드 될수 있도록 돕고 확대나 축소를 허용할 것인지 결정 해줌.

뷰포트는 장치에 따라 다름 (휴대폰화면은 컴퓨터 화면 보다 작음)

### Media query

media query는 화면의 종류와 크기에 따라서 디자인을 달리 줄 수 있는 CSS의 기능.

특히 최근의 트랜드인 반응형 디자인의 핵심 기술이라고 할 수 있음.

#### 기본구성(syntax)

------

```
@media only|not mediatype and|not|,(or) (media feature) { CSS스타일코드;}
```

- not: 부정
- only: 말 그대로 only; 이것만
- media type(매체유형)
  - all(모든 미디어; 기본값)
  - screen(화면이 달린 기기; 스마트폰, 태블릿 PC등)
  - print(프린터 기기)
  - braille(점자표시장치)
  - tv(음성과 영상이 동시 출력되는 TV)
- and 또는 , (or): 조건
- media feature(표현식): 특정 조건을 입력. 예) `min-width: 800px`

#### Media query의 대표적인 조건

------

**width**

- viewport의 너비를 의미하며, 일반적으로 가장 많이 사용 하는 조건.
- h2 태그의 색상을 기본적으로 녹색으로 설정하며, 너비가 800px이 되면, 노란색으로 색상이 변경됨

```
h2 {
    color: green;
}

@media (width: 800px) {
    h2 {
        color: yellow;
    }
}
```

**min-width / max-width**

- h3태그의 기본 색상은 회색
- viewport의 너비가 min 600 px 와 max 800 px 조건을 만족할 경우, 색상이 보라색으로 변경됨

```
h3 {
    color:gray;
}

@media (min-width:600px) and (max-width: 800px) {
    h3 {
        color: purple;
    }
}
```

**height / min-height / max-height**

- h4 태그의 기본색상은 Orange
- viewport의 높이(세로 길이)가 min 400 px 와 max 600 px을 만족할 경우, 색상은 검정으로 변경됨

```
h4 {
    color: orange;
}
@media (min-height: 400px) and (max-height: 600px) {
    h4 {
        color: black;
    }
}
```

**orientation**

- 가상 선택자 `::after` 을 활용하여, view port의 방향에 따라 조건 적용
- view port의 방향이 가로일때는 '가로입니다' 출력
- view port의 방향이 세로일때는 '세로입니다' 출력

```
h1.ori::after {
    content: '가로입니다'

}

@media (orientation: portrait) {
    h1.ori::after {
        content: '세로입니다.'
    }
}
```

**응용: Bootstrap의 Break point 흉내내기**

```
/* Extra small: 0~576px */
.rainbow {
    color: red;
}

/* Small: 576px 이상 */
@media (min-width: 576px) {
    .rainbow {
        color: orange;
    }
}

/* Medium: 768px 이상 */
@media (min-width: 768px) {
    .rainbow {
        color: yellow;
    }
}

/* Large: 992px 이상 */
@media (min-width: 992px) {
    .rainbow {
        color: green;
    }
}

/* Extra Large: 1200px 이상 */
@media (min-width: 1200px) {
    .rainbow {
        color: blue;
    }
}
```

### break point

Bootstrap의 break point를 활용하여 view port의 width에 따라 컬럼 갯수를 다르게 설정할 수 있음.

- 576px보다 작을 때: col-12 조건 적용 => 한줄에 12칸을 차지하는 박스 생성 (총 12줄)
- 576px보다 클때: col-sm-6 조건 적용 => 한줄에 6칸을 차지하는 박스 생성 (총 6줄)
- 768px보다 클때: col-md-4 조건 적용 => 한줄에 4칸을 차지하는 박스 생성 (총 4줄)
- 992px보다 클때: col-lg-3 조건 적용 => 한줄에 3칸을 차지하는 박스 생성 (총 3줄)
- 1200px 보다 클때: col-xl-2 조건 적용 => 한줄에 2칸을 차지하는 박스 생성 (총 2줄)

상기 조건을 활용하여, view point에 따라 박스를 숨기는 등의 추가적인 속성도 적용 가능

- view port가 small(576px ~ 768px) 일 경우, 마지막 박스는 숨겨짐

```
<div class="container">
    <div class="row">
        <div class="d-sm-none col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">01</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">02</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">03</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">04</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">05</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">06</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">07</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">08</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">09</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">10</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">11</div>
        <div class="d-sm-none col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">12</div>
    </div>
</div>
```

*Bootstrap의 breakpoint*

> [![breakpoint](https://camo.githubusercontent.com/c2ad9dcc62850c9310723414b758dea1d5e33358/68747470733a2f2f77706d61737465722e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031372f30322f626f6f7473747261702d342d677269642e6a7067)](https://camo.githubusercontent.com/c2ad9dcc62850c9310723414b758dea1d5e33358/68747470733a2f2f77706d61737465722e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031372f30322f626f6f7473747261702d342d677269642e6a7067)