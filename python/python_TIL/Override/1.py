class C1:
    def m(self):
        return 'parent'


class C2(C1):
    def m(self):
        return super().m() + ' child'   # 부모클래스를 의미하는 super의 메서드


o = C2()
print(o.m())