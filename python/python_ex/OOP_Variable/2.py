class C:
    def __init__(self, v):
        self.value = v

    def show(self):
        print(self.value)

    def getValue(self):
        return self.value

    def setValue(self,v):
        self.value = v


        
c1 = C(10)
print(c1.getValue())

c1.setValue(c1.getValue())
print(c1.getValue())

c1.show()




## 생활코딩 85부터듣기