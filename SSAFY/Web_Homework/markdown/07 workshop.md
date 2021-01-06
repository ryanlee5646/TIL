```python
class Circle():
    pi = 3.14
    x = 0
    y = 0
    r = 0
    
    def area(self):
   	 	return self.pi * self.r * self.r
	
	def circumference(self):
    	return 2 * self.pi * self.r
	
	def center(self):
   		return (self.x, self.y)
	
	def move(self, x, y):
    	self.x = x
    	self.y = y
```

```python

python
l = Circle()
l.r = 3
l.move(2,4)
l.center()
print(f'원의 넓이는 : {l.area()}')
print(f'원의 둘레는 : {l.circumference()}')
```

