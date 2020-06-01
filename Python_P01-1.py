r = float(input("원의 반지름을 입력하세요. >> "))
PI = 3.141592

if r < 0 :
    print("잘못된 입력입니다.")
else :
    print("원의 넓이:",(r*r*PI))
    print("원의 둘레:",(2*r*PI))
