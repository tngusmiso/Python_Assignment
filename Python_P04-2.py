# 입력받은 문자열을 '-'문자 기준으로 split하여 리스트에 저장
birthday = input('생년월일을 "2001-03-01" 형식으로 입력하세요:').split('-')
print("생년월일:",birthday[0]+"년", birthday[1]+"월", birthday[2]+"일")

# 입력받은 생일의 년도를 int형으로 형변환하여 나이를 계산
age = 2020 - int(birthday[0]) + 1
print("나이:",str(age)+"세")
