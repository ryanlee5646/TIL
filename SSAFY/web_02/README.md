## 01_layout

```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>영화추천사이트</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous"> 
    <link rel="stylesheet" href="01_layout.css">
    <link href="https://fonts.googleapis.com/css?family=Cute+Font|Stylish" rel="stylesheet">

<link href="https://fonts.googleapis.com/css?family=Cute+Font|Jua|Nanum+Gothic+Coding|Stylish" rel="stylesheet">
 구글폰트 호출

    
 *부트스트랩 호출, 01_layout.css파일 호출
 google 폰트 호출

/* nabar 타이틀 폰트 */
 .font1 {
    font-family: 'Stylish', sans-serif;
    font-size: 50px;
}
/* navbar 메뉴폰트 */
.font2 {
    font-family: 'Cute Font', cursive;
    font-size: 40px;
    color: whitesmoke ;
}

/* footer 'top' 폰트 */
.font3{
    font-family: 'Cute Font', cursive;
    font-size: 30px;
    color: whitesmoke !important;

```







## 02_movie

```html
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
        <a class="navbar-brand font2 font1" href="#">영화추천시스템</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav"
            aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto font2">
                <li class="nav-item active ">
                    <b><a class="nav-link" href="#">Home<span class="sr-only">(current)</span></a></b>
                </li>
                <li class="nav-item ">
                    <a class="nav-link" href="#">친구 평점 보러가기</a>
                </li>
                <li class="nav-item ">
                    <a class="nav-link" href="#">Log in</a>
                </li>
            </ul>
        </div>
    </nav>
    
카드 생성및/ 폰트 적용
```







## 03_detail_view

```html
  <img src="images/malmoe.jpg" class="card-img-top" alt="malmoe" data-toggle="modal" data-target="#malmoe">
# Modal 호출

<div class="modal fade" id="malmoe" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">말모이</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <img src="images/malmoe1.jpg" alt="malmoe">
                <div class="modal-body">
                    <p>줄거리
 </p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
                </div>
            </div>
        </div>
    </div>
Modal 내용
```

