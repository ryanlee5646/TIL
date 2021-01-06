```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        <button v-on:click="counter++">+1</button> <!-- count를 올려주는 수식 -->
        <h1>Counter: {{ counter }}</h1>

    </div>
    <script>
            const app = new Vue({
                el: '#app', 
                data: { 
                    counter: 0,
                },
            })
        </script>
</body>
</html>
```



