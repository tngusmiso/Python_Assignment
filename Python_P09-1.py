infile = open("score.txt","r")
outfile = open("avg.txt","w")

for line in infile:

    # 단어 단위로 저장
    line = line.rstrip()
    word_list = list(line.split(','))
    num =0

    # word_list의 인덱스 0은 이름이므로
    # word_list의 인덱스 1부터 정수의 합을 구한다.
    for i,val in enumerate(word_list[1:]):
        num += int(val)

    # 평균을 구하여 문자열에 저장
    result ="{}의 평균: {}\n".format(word_list[0], num/len(word_list[1:]))

    # 문자열을 파일에 작성
    outfile.write(result)

infile.close()  
outfile.close()
