class Cs:
    #클래스메서드 선언
    @staticmethod
    def static_method():
        print("Static method")

    #클래스에 소속된 클래스 메서드
    @classmethod
    def class_method(cls):
        print("Class method")

    def instance_method(self):
        print("Instance method")



i = Cs()

Cs.static_method()

.class_method()

i.instance_method()