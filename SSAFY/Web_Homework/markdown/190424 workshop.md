```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <script>
    const url = 'http://13.125.249.144:8080/ssafy/gumi/1/posts'
    // 1. GET
    axios.get(url) // get 요청을 보냈는데
            .then(function(response){ // 응답이 온다면
                console.log(response.data)
            })

    // 2. POST
    axios.post(url, {
        post: {
            title: 'Avengers',
            content: 'I am Ironman',
            author: 'Ruso brothers'
        }
    })
    .then (function(resposne){
        console.log(response.data)
    })
    </script>
</body>
</html>
```

