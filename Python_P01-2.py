score = int(input("점수를 입력하세요. >> "))

if score<0 or score>100:
    print("잘못된 입력입니다.")
elif score>=95:
    print("A+")
elif score>=90:
    print("A0")
elif score>=85:
    print("B+")
elif score>=80:
    print("B0")
elif score>=75:
    print("C+")
elif score>=70:
    print("C0")
elif score>=65:
    print("D+")
elif score>=60:
    print("D0")
else:
    print("F")
