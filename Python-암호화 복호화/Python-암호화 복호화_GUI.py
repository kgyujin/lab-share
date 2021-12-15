from tkinter import *
from functools import partial

def func(secu):
    inFp = open(infile.get(), "r", encoding="UTF8")
    outFp = open(outfile.get(), "w", encoding="UTF8")

    while True:
        inStr = inFp.readline()
        if not inStr:
            break

        outStr = ""
        for i in range(0, len(inStr)):
            ch = inStr[i]
            chNum = ord(ch)
            chNum = chNum + secu
            ch2 = chr(chNum)
            outStr = outStr + ch2

        outFp.write(outStr)

    outFp.close()
    inFp.close()
    lab3.configure(text="%s --> %s 변환 완료" % (infile.get(), outfile.get()))

root = Tk()

lab1 = Label(root, text="입력 파일명")
lab1.grid(column=0, row=0)
lab2 = Label(root, text="출력 파일명")
lab2.grid(column=0, row=1)

infile = StringVar()
outfile = StringVar()
path1 = Entry(root, width=32, textvariable=infile)
path1.grid(column=1, row=0)
path2 = Entry(root, width=32, textvariable=outfile)
path2.grid(column=1, row=1)

btn1 = Button(root, text="암호화", command=partial(func, 100))
btn1.grid(column=2, row=0)
btn2 = Button(root, text="복호화", command=partial(func, -100))
btn2.grid(column=2, row=1)

lab3 = Label(root, text="파일명을 입력하세요")
lab3.grid(column=1, row=2)

root.mainloop()
