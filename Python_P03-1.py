length = len(input("비밀번호 입력: ")) # 입력받은 비밀번호의 문자열의 길이 저장

# 문자열의 길이가 10 이상
if length >= 10: 
    safety = "좋음"

# 문자열의 길이가 10 미만 5 이하
elif length >= 5: 
    safety = "보통"

# 문자열의 길이가 5 미만 
else: 
    safety = "나쁨"

print("비밀번호 안전도: ", safety)
