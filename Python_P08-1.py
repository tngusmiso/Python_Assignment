
import math

class Polygon:

    # 생성자
    def __init__(self, length):
        self.__length = length

    # 접근자 
    def getLength(self):
        return self.__length

    # 메소드 (구현x)
    def area(self):
        pass
    
    def peri(self):
        pass

    # 오버라이드
    def __str__(self):
        return "종류 : {}\n길이 : {}\n넓이 : {}\n둘레 : {}\n".format(type(self).__name__, self.getLength(), self.area(), self.peri())

class Triangle(Polygon):

    # 생성자 
    def __init__(self, length):
        super().__init__(length)

    # 메소드 
    def area(self):
        super().area()
        return (math.sqrt(3) / 4) * math.pow(super().getLength(), 2)
    
    def peri(self):
        super().peri()
        return super().getLength() * 3

class Square(Polygon):

    # 생성자
    def __init__(self, length):
        super().__init__(length)
        
    # 메소드 
    def area(self):
        super().area()
        return math.pow(super().getLength(), 2)
    
    def peri(self):
        super().peri()
        return super().getLength() * 4

e1 = Triangle(10)
print(e1)

e2 = Square(20)
print(e2)
