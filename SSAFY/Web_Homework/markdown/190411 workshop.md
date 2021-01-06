**Django에서 myapp의 Musician class에 저장된 기본 시드데이터이다. 이를 적용하기 위해 필요한 json파일을 만들어 적용해보자.**

`python manage.py dumpdata myapp.musician --indent 2 > musician.json`

```json
[	

​	{

​		"pk":1,

​		"model" : "myapp.musician",

​		"fields":{

​			"first_name":"John",

​			"last_name":"Lennon"

​		}

​	},

​	{

​		"pk":2,

​		"model" : "myapp.musician",

​		"fields":{

​			"first_name":"Paul",

​			"last_name":"McCartney"

​		}

​	},

]
```

