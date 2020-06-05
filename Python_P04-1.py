print("### 회원 등록 프로그램 ###")
print("### 0 입력시 입력 종료 ###")

members = []

# 무한 반복으로 이름 입력
while True:
    name = input("회원 이름 입력: ")

    # 입력받은 내용이 '0'이면 입력 종료
    if name == "0":
        print("회원 등록 완료!")
        break

    # 입력 받은 내용이 '0'이 아니면 리스트에 추가
    members.append(name)
        

print("회원 명부 출력 (등록순서):", members)  # 리스트 출력
print("회원 명부 출력 (오름차순):", sorted(members))  # 리스트 오름차순 정렬 
print("회원 명부 출력 (내림차순):", sorted(members, reverse = True))  # 리스트 정렬 후 순서 뒤집기 
