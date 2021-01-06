1.

```python
my_list = [1,2,3,4,5,6,7]
for i in my_list:
    print(i)
```

2.

``` python
#방법1
my_list = [1,2,3,4,5,6,7]
for j in range(len(my_list)):
    print(j, my_list[j])
#방법2
for k,g in enumerate(my_list):
    print(k,g) '''
```

3.

``` python
lunch =
{ 
  '중국집':'02-123-123',
  '양식집':'054-123-123',
  '한식집':'031-123-123'
}
```

key:  

`for key in lunch`
value:  

`for value in lunch.keys()`
key와 value:  

`for key,value in lunch.items()`

4.

``` python
def my_func(a, b):
    c = a + b
    print(c)
result = my_func(1, 5)```
```

=> None