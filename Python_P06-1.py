class Employ:

    # 생성자
    def __init__(self, name, year, degree):
        self.__name = name
        self.__year = year
        self.__degree = degree

    # 접근자
    def getName(self):
        return self.__name
    def getYear(self):
        return self.__year
    def getDegree(self):
        return self.__degree

    # 설정자
    def setName(self, name):
        self.__name = name
    def setYear(self, year):
        self.__year = year
    def setDegree(self, degree):
        self.__degree = degree

    # 메소드  
    def salary(self):
        if self.__degree == "학사":
            return self.__year*100 + 3000
        if self.__degree == "석사":
            return self.__year*100 + 3500
        if self.__degree == "박사":
            return self.__year*100 + 4000

    def show(self):
        print("이름:", self.getName())
        print("연차:", str(self.getYear()))
        print("학위:", self.getDegree())
        print("연봉:", str(self.salary()), "만원")

# 코드상에서 객체로 생성하는 경우 
e1 = Employ("브라보", 10, "박사")
e1.show()
print()

e2 = Employ("부싯돌", 5, "석사")
e2.show()
print()

e3 = Employ("홍길동", 2, "학사")
e3.show()
print()

# 직접 입력하는 경우
while True:
    print("직접 입력해보세요. 종료를 원하면 0을 입력하세요")
    my_name = input("이름: ")

    if my_name == "0":
        break
    
    my_year = int(input("연차: "))
    my_degree = input("학위: ")
    me = Employ(my_name, my_year, my_degree)
    print("연봉:", str(me.salary()), "만원")
    print()
    
print("종료합니다.")

