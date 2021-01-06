아래 Python코드를 JS코드로 변환해보자. Checkpoint

1. **브라우저는 생각하지 않는다.** 
2.  **변수/함수이름은JSnaming convention(lowerCamelCase)을 따른다.**
3. **F String=>Template Literal.**

```python
# This is Comment

def concat(str1, str2):
    return f'{str1} - {str2}'

def check_long_str(string):
    if len(string) > 10:
        return True
    else:
        return False
 
if check_long_str(concat('Happy', 'Hacking')):
    print('LONG STRING')
 else:
    print('SHORT STRING')
```

```js
// JS Code
function conCat(str1, str2){
    return `${str1} - ${str2}`
}

function checkLongStr(string){
    if (string.length > 10){
        return True
    }else{
        return False
    }
}

if (checkLongStr(conCat('Happy', 'Hacking'))){
    console.log('LONG STRING')
} else{
	console.log('SHORT STRING')
}
```

