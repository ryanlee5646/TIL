```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>0</h1>h1>
    <button id="change-btn">Click it</button>
    <script>
       const button = document.querySelector('#change-btn')
       const header = document.querySelector('h1')
       let clickCount = 0
       button.addEventListener('click', function(event){
           clickCount+=1
           header.innerText = `${clickCount}`
       })
    </script>
</body>
</html>
```
