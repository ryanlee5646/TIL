**항상 CDN으로만 사용해왔던 Bootstrap을 이번에는 직접CSS,  JS 파일로 다운로드 받아Django Project에 정적 파일로 추가하고 사용해보자.**

```static 폴더안에 bootstrap.css 파일 추가```

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'bootstrap.css' %}" type="text/css" />
</head>
```

**적용하고자하는 html에 링크 추가**

