# 본 코드는 교수님께서 작성하신 코드를 그대로 옮긴 파이썬 코드 파일입니다.
# 암호화와 복호화를 설정하는 라디오 버튼에 관련된 코드는 첨부되어 있지 않습니다.
from tkinter import *
from functools import partial

def def_func(aa):
    print(aa)

window = Tk()
# window.geomerty("210x210")

lab1 = Label(window, text="입력 파일명")
lab1.grid(column=0, row=0)
lab2 = Label(window, text="출력 파일명")
lab2.grid(column=0, row=1)

infile = StringVar()
outfile = StringVar()
textbox1 = Entry(window, width=32, textvariable=infile)
textbox1.grid(column=1, row=0)
textbox2 = Entry(window, width=32, textvariable=outfile)
textbox2.grid(column=1, row=1)

btn1 = Button(window, text="암호화", command=partial(def_func, 100))
btn1.grid(column=2, row=0)
btn2 = Button(window, text="복호화", command=partial(def_func, -100))
btn2.grid(column=2, row=1)

window.mainloop()
