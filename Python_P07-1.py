from tkinter import *

# 회원정보 딕셔너리에 저장
user = {'김선형':'1234', '임수현':'5678'}

# 로그인 함수 
def login():
    userID = IDEntry.get()
    userPW = PWEntry.get()
    if userID not in user:
        loginLabel["text"] = "로그인 실패(ID 오류)"
    elif user[userID] != userPW:
        loginLabel["text"] = "로그인 실패(PW 오류)"
    else:
        loginLabel["text"] = "로그인 성공"

# 초기화 함수 
def reset():
    IDEntry.delete(0,'end')
    PWEntry.delete(0,'end')
    loginLabel["text"] = "로그인 하세요."

# 윈도우 설정 
window = Tk()
window.title("등록 확인")

loginLabel = Label(window, text="로그인 하세요.", bg="pink", fg="yellow") #배경색과 글자색 지정

IDLabel = Label(window, text="ID를 입력하세요.")
IDEntry = Entry(window)

PWLabel = Label(window, text="비밀번호를 입력하세요.")
PWEntry = Entry(window, show='*') #비밀번호 입력 시 *로 표시

logintButton = Button(window, text="로그인", command=login)
resetButton = Button(window, text="초기화", command=reset)

# 배치 관리 (grid)
loginLabel.grid(row=0, columnspan=2, sticky=W+E)
IDLabel.grid(row=1, columnspan=2, sticky=W+E)
IDEntry.grid(row=2, columnspan=2, sticky=W+E)
PWLabel.grid(row=3, columnspan=2, sticky=W+E)
PWEntry.grid(row=4, columnspan=2, sticky=W+E)
logintButton.grid(row=5, column=0, sticky=W+E)
resetButton.grid(row=5, column=1, sticky=W+E)

window.mainloop()
