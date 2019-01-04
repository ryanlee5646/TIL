# class Service:
#         secret = "영구는 배꼽이 두 개다." 
#         def setname(self, name):
#                 self.name = name
#         def sum(self, a, b):
#                 result = a + b
#                 print(f"{self.name}님 {a}+{b} ={result}입니다")
        
# pey = Service()
# pey.setname("홍길동")
# pey.sum(1,1)

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
            result = self.first + self.second
            return result                            
a = FourCal(4,2)

print(a.sum())

