# CookBook Python에 있는 라디오 버튼 코드 예시
# tkinter 모듈 불러옴
from tkinter import *

# myFunc()라는 이름의 함수 생성
# configure(옵션=값) 함수를 통해 해당 위젯의 옵션값이 변경되게함
def myFunc():
    if var.get() == 1:
        # var의 값이 1일 경우, 레이블 label1의 text를 "파이썬"으로 변경
        label1.configure(text="파이썬")
    elif var.get() == 2:
        # var의 값이 2일 경우, 레이블 label1의 text를 "C++"으로 변경
        label1.configure(text="C++")
    else:
        # var의 값이 1이나 2 외일 경우, 레이블 label1의 text를 "Java"으로 변경
        label1.configure(text="Java")

# Tk()를 통해 window라는 객체변수에 윈도우를 반환
window = Tk()

var = IntVar()
# 라디오버튼 rb1을 선택시 value의 값을 객체변수 var에 입력
rb1 = Radiobutton(window, text="파이썬", variable=var, value=1, command=myFunc)
# 라디오버튼 rb2을 선택시 value의 값을 객체변수 var에 입력
rb2 = Radiobutton(window, text="C++", variable=var, value=2, command=myFunc)
# 라디오버튼 rb3을 선택시 value의 값을 객체변수 var에 입력
rb3 = Radiobutton(window, text="Java", variable=var, value=3, command=myFunc)

label1 = Label(window, text="선택한 언어 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

# window라는 객체변수에서의 이벤트 발생을 위한 코드인 mainloop() 함수 실행
window.mainloop()
