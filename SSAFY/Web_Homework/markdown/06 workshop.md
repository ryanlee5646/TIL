양의 정수 x를 입력받아 제곱근의 근사값의 결과를 반환하는 함수를 

작성하세요.
sqrt() 사용금지

``` python
def binary_search(num):
    low = 1
    high = num
    result = 1
    while abs(high-low) > 0.000001:
        result = (low+high)/2
        if result**2 < num:
            low = result
        else: 
            high = result
    return result
```



