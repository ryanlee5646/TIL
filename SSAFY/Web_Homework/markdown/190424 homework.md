```python
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
        const url = 'https://dog.ceo/api/breeds/image/random'
        
        axios.get(url)
                .then(function(response){
                    const imgSrc = response.data.message
                    return imgSrc
                })
                .then(function(imageSource){
                    console.log(imageSource)
                })
    
    </script>
    
</body>
</html>
```
