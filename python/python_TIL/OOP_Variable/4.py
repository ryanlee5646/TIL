class C:
    def __init__(self, v):
        # 객체 변수에 접근할 수 없게 변수 앞에 '__' 붙이기
        self.__value = v

    def show(self):
        print(self.value)

        
c1 = C(10)

print(c1.value)