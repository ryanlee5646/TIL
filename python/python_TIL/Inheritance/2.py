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

# Cal클래스에 있는 생성자를 상속받을 뿐만아니라 메서드도 모두 상속받는다.
#=> 재활용성 
        
class CalMultiply(Cal):
    def multiply(self):
        return self.v1 * self.v2

class CalDivide(CalMultiply):
    def divide(self):
        return self.v1 / self.v2


c1 = CalMultiply(10, 10)

print(c1.add())
print(c1.multiply())

c2 = CalDivide(20,10)

print(c2.add())
print(c2.multiply())
print(c2.divide())