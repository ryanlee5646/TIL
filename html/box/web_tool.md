# DAY08

## 웹 Intro

- 모든 웹은 주소로 요청을 하고 서버로부터 문서(1장)로 응답을 받는다.
- [www.naver.com](http://www.naver.com/)
- 인기검색어 1위 '우클릭'- '검색' 하고 검색어를 'DAY'로 수정하면 검색어 1위가 DAY로 바뀐다. 수정된 문서 값에 맞춰서 문서의 값들을 보여주는 웹 화면에서 나타난다

## Flask

- `pip install flask`: flask 설치

- ```
  FLASK_DEBUG=1 FLASK_APP=hello.py flask run
  ```

  : Flask Run

  - 서버를 종료하지 않아도 수정된 소스파일을 저장하면 수정사항이 적용돼서 주소만 새로 입력하면 된다.

- 주소의 입력이 달라져야할 때 variable routing을 사용한다.

  - `@app.rout('/dictionary/<string:word>')`
  - `<int:word> <path:word>`도 된다

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