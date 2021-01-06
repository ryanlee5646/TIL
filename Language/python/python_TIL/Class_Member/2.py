class Cs:
    count = 0 # 클래스 안에 변수 선언(클래스에 소속된 클래스 변수)
    def __init__(self):
        Cs.count = Cs.count + 1 # 클래스 이름뒤에 .을 붙여서 클래스 변수에 접근

    # 인스턴스 메서드가아닌 클래스에 속한 메스드라고 선언
    @classmethod
    def getCount(self):
        print(self)
        return Cs.count




i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()

print(Cs.getCount())