class Cal:
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1

        if isinstance(v1, int):    
            self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

    def setV1(self,v):
        if isinstance(v, int): # 인자값 인스턴스를 체크
            self.v1 = v

    def getV1(self):
        return self.v1


        
c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

# c1.v1 = 'one'
# c1.v2 = 30

print(c1.add())

print(c1.subtract())

c1.setV1(20)
c1.setV1('one')
print(c1.getV1())

