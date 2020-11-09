class C1():
    def c1_m(self):
        print("c1_m")

    def m(self):
        print("C1 m")

class C2():
    def c2_m(self):
        print("c2_m")

    def m(self):
        print("C2 m")

class C3(C2, C1): # 앞쪽에 선언된 부모가 우선 순위
    def m(self):
        print("C3 m")


c = C3()

c.c1_m()
c.c2_m()
c.m()

print(C3.__mro__) # C3의 부모클래스 우선순위