print("=== 1:덧셈 2:뺄셈 3:곱셈 4:나눗셈 0:종료 ===")

while True: #무한 루프
    
    op = int(input("연산 입력: "))

    if op < 0 or op > 4: # 연산이 0,1,2,3,4가 아닐 경우 다시 입력받기
        print("잘못된 입력입니다.")
        continue

    elif op == 0: # 종료 조건
        break

    print("숫자 입력: ")
    num1 = float(input())
    num2 = float(input())

    if op == 1: # 덧셈연산 
        answer = num1+num2
        
    elif op == 2: # 뺄셈연산  
        answer = num1-num2
        
    elif op == 3: # 곱셈연산 
        answer = num1*num2
        
    elif op == 4: # 나눗셈연산 
        answer = num1/num2
        
    print("연산 결과: ", answer)
    
print("연산 종료")
