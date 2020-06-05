wordDic = {}

# 무한 루프
while True:
    wordEng = input("영어 단어 : ")

    # 빈 문자열이 입력되면 반복문 탈출
    if wordEng == "":
        break

    # 사전이 비어있는 경우 
    if not wordDic:
        print("사전이 비어 있습니다.")

    # 등록되지 않은 경우 
    elif not wordEng in wordDic:
        print(wordEng, "단어가 등록되어있지 않습니다.")

    # 등록 되어있는 단어일 경우 한글단어 출력 
    else:
        print("한글단어 :", wordDic[wordEng])
        continue

    #단어 등록 
    print("단어를 추가합니다.")
    wordKor = input("한글 단어 : ")
    wordDic[wordEng] = wordKor

# 전체 단어 출력
print(wordDic)
