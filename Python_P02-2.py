sum = 0.0

while True:
    value = input("입력하시겠습니까?(Y/N) : ")

    if value == 'Y':
        number = float(input("숫자를 입력하세요. : "))
        sum += number

    elif value == 'N':
        break

    else:
        print("잘못된 입력입니다. Y 또는 N을 입력하세요.")

print("덧셈 결과 : ",sum)
