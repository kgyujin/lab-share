from tkinter import *
from tkinter import messagebox
import sqlite3


def insertdata() :
    con = sqlite3.connect('E:\\수업자료\\SQLite\\nation')
    cur = con.cursor()

    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get(); data5 = edt5.get()
    if data1 != '' and data2 != '' and data3 != '' and data4 != '' and data5 != '' :
        try :
            sql = 'insert into 국가 values ("'+data1+'", "'+data2+'", "'+data3+'", "'+data4+'", "'+data5+'")'
            cur.execute(sql)
        except :
            messagebox.showinfo('오류', '입력 오류')
        else :
            messagebox.showinfo('성공', '입력 성공')
    else :
        messagebox.showinfo('Not Null','공백을 확인하세요')
    
    con.commit()
    selectdata()
    # con.close()

def selectdata() :
    con = sqlite3.connect('E:\\수업자료\\SQLite\\nation')
    cur = con.cursor()
    
    strdata1, strdata2, strdata3, strdata4, strdata5 = [], [], [], [], []
    cur.execute('select * from 국가')

    strdata1.append('이름'); strdata2.append('영문이름'); strdata3.append('지역'); strdata4.append('인구'); strdata5.append('GDP')
    strdata1.append('----------'); strdata2.append('----------'); strdata3.append('----------'); strdata4.append('----------'); strdata5.append('----------')
    
    while (True) :
        row = cur.fetchone() #한행씩 추출해서 튜플형식으로 저장
        if row == None :
            break
        strdata1.append(row[0]); strdata2.append(row[1]); strdata3.append(row[2]); strdata4.append(row[3]); strdata5.append(row[4])

    listdata1.delete(0, listdata1.size()-1); listdata2.delete(0, listdata2.size()-1);
    listdata3.delete(0, listdata3.size()-1); listdata4.delete(0, listdata4.size()-1); listdata5.delete(listdata5.size()-1)
    for item1, item2, item3, item4, item5 in zip(strdata1, strdata2, strdata3, strdata4, strdata5) :
        listdata1.insert(END, item1); listdata2.insert(END, item2);
        listdata3.insert(END, item3); listdata4.insert(END, item4); listdata5.insert(END, item5);  

    con.close()

def deletedata() :
    con = sqlite3.connect('E:\\수업자료\\SQLite\\nation')
    cur = con.cursor()
    pri = listdata1.get(ANCHOR)
    data = edt1.get()
    
    # try :
    #     sql = 'delete from 국가 where 이름 = "'+pri+'"'
    #     cur.execute(sql)
    # except :
    #     messagebox.showinfo('실패', '삭제 실패')
    # else :
    #     messagebox.showinfo('성공', '삭제 성공')
    
    try :
        sql = 'delete from 국가 where 이름 = "'+data+'"'
        cur.execute(sql)
    except :
        messagebox.showinfo('실패', '삭제 실패')
    else :
        messagebox.showinfo('성공', '삭제 성공')

    con.commit()
    selectdata()
    
    # con.close()

def updatedata() :
    con = sqlite3.connect('E:\\수업자료\\SQLite\\nation')
    cur = con.cursor()
    
    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get() ; data5 = edt5.get()   
    
    try :
        sql = 'update 국가 set 영문이름 = "'+data2+'", 지역 = "'+data3+'", 인구 = "'+data4+'", GDP = "'+data5+'" where 이름 = "'+data1+'"'
        cur.execute(sql)
    except :
        messagebox.showinfo('실패', '업데이트 실패')
    else :
        messagebox.showinfo('성공', '업데이트 성공')
    
    con.commit()
    selectdata()
    
    # con.close()

window = Tk()
window.title('sql')
# window.geometry('')

edtFrame = Frame(window)
edtFrame.pack()

btnFrame = Frame(window)
btnFrame.pack()

listFrame = Frame(window)
listFrame.pack(fill=BOTH, expand=1)


lebel1 = Label(edtFrame, width=15, text='이름')
lebel1.grid(row=0, column=0)
lebel2 = Label(edtFrame, width=15, text='영문이름')
lebel2.grid(row=0, column=1)
lebel3 = Label(edtFrame, width=15, text='지역')
lebel3.grid(row=0, column=2)
lebel4 = Label(edtFrame, width=15, text='인구')
lebel4.grid(row=0, column=3)
lebel5 = Label(edtFrame, width=15, text='GDP')
lebel5.grid(row=0, column=4)

edt1 = Entry(edtFrame, width=20, bg='#DFE7FF');
edt1.grid(row=1, column=0, padx=2, ipady=2)
edt2 = Entry(edtFrame, width=20, bg='#DFE7FF');
edt2.grid(row=1, column=1, padx=2, ipady=2) 
edt3 = Entry(edtFrame, width=20, bg='#DFE7FF');
edt3.grid(row=1, column=2, padx=2, ipady=2) 
edt4 = Entry(edtFrame, width=20, bg='#DFE7FF');
edt4.grid(row=1, column=3, padx=2, ipady=2)
edt5 = Entry(edtFrame, width=20, bg='#DFE7FF');
edt5.grid(row=1, column=4, padx=2, ipady=2)

btninsert = Button(btnFrame, text='입력', width=20, command=insertdata)
btninsert.grid(row=0, column=0, padx=10, pady=10)
btnselect = Button(btnFrame, text='조회', width=20, command=selectdata)
btnselect.grid(row=0, column=1, padx=10, pady=10)
btndelete = Button(btnFrame, text='삭제', width=20, command=deletedata)
btndelete.grid(row=0, column=2, padx=10, pady=10)
btnupdate = Button(btnFrame, text='수정', width=20, command=updatedata)
btnupdate.grid(row=0, column=3, padx=10, pady=10)


listdata1 = Listbox(listFrame, bg='white')
listdata1.pack(side=LEFT, fill=BOTH, expand=1)
listdata2 = Listbox(listFrame, bg='white')
listdata2.pack(side=LEFT, fill=BOTH, expand=1)
listdata3 = Listbox(listFrame, bg='white')
listdata3.pack(side=LEFT, fill=BOTH, expand=1)
listdata4 = Listbox(listFrame, bg='white')
listdata4.pack(side=LEFT, fill=BOTH, expand=1)
listdata5 = Listbox(listFrame, bg='white')
listdata5.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()