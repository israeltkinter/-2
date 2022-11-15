import tkinter as tk
from tkinter import ttk
import random
from tkinter import *
import win32api

# window
root = tk.Tk()
root.geometry("900x600")
root.title("כתיבה ישר והפוך")
root.configure(bg="white")
root.resizable(False,False)


one1 = tk.StringVar()
one2 = tk.StringVar()
one3 = tk.StringVar()
one4 = tk.StringVar()
#commands
def send():
    win32api.ShellExecute(0,'open','mailto:',None,None ,0)

def showmessage(title_box:str=None, message:str=None):
    TIME_TO_WAIT = 900
    new = Toplevel(root)
    background='green'
    new.geometry('200x30+100+300')
    new.configure(bg="white")
    new.title(title_box)
    Label(new, text=message, background=background, font=("Ariel", 15), fg="white").pack(padx=4, pady=2)
    try:
        new.after(TIME_TO_WAIT, new.destroy)
    except Exception as e:
        print('Error occured', e)



def copya():
    by = one2.get()
    label1.clipboard_clear()
    label1.clipboard_append(by)
    message = "הועתק"
    title = "העתקה"
    showmessage(title, message)
    
    


def copyb():
    by = one4.get()
    label1.clipboard_clear()
    label1.clipboard_append(by)
    message = "הועתק"
    title = "העתקה"
    showmessage(title, message)

def copyc():
    by = one1.get()
    label1.clipboard_clear()
    label1.clipboard_append(by)
    message = "הועתק"
    title = "העתקה"
    showmessage(title, message)
    
def copyd():
    by = one3.get()
    label1.clipboard_clear()
    label1.clipboard_append(by)
    message = "הועתק"
    title = "העתקה"
    showmessage(title, message)    
        
    

def one():
    get1 = input1.get()
    get2 = input2.get()
    label1 = tk.Label(frame2, textvariable=one2,bg="white")
    label1.place(x=50,y=0)
    one2.set(f'{get1} \n {get2}')
        
    

def two():
    get1 = input1.get()
    get2 = input2.get()
    label1 = tk.Label(frame3, textvariable=one4,bg="white")
    label1.place(x=50,y=0)
    one4.set(f'{get2} \n {get1}'[::-1])


def three():
    get1 = input1.get()
    get2 = input2.get()
    label1 = tk.Label(frame4, textvariable=one1,bg="white")
    label1.place(x=50,y=0)
    one1.set(f'{get2} \n {get1}'[::-1])

def four():
    get1 = input1.get()
    get2 = input2.get()
    L = list(get1)
    random.shuffle(L)
    shuffled = "".join(L)
    M = list(get2)
    random.shuffle(M)
    shuffled = "".join(M)
    label1 = tk.Label(frame5, textvariable=one3,bg="white")
    label1.place(x=50,y=0)
    one3.set(f'{L} \n {M}')



#label
label1 = tk.Label(root, text="יישור כתיבה לכל הכיוונים", bg="white",font=("Ariel",25,"bold"))
label1.place(x=300,y=0)
label9 = tk.Label(root, text="< הקלד טקסט להדבקה", bg="white",font=("Ariel",12,"bold"))
label9.place(x=715,y=100)
label2 = tk.Label(root, text="< הקלד טקסט לראייה", bg="white",font=("Ariel",12,"bold"))
label2.place(x=715,y=130)
label3 = tk.Label(root, text="ת\nו\nצ\nא\nה",bg="white",font=("Ariel",25,"bold"))
label3.place(x=750,y=320)
label4 = tk.Label(root, text="או",bg="white",font=("Ariel",15))
label4.place(x=505,y=175)
label5 = tk.Label(root, text="אהבתם את התוכנה\nשלחו דואר אל יוצר התוכנה   ",bg="white",font=("Ariel",12))
label5.place(x=0,y=0)
label6 = tk.Label(root, text="ymb6143@gmail.com",bg="white",font=("Microsoft Yhaei UI Light",12))
label6.place(x=0,y=40)

#entry
input1 = ttk.Entry(root, width=62)
input1.place(x=330,y=100,height=30)
input2 = ttk.Entry(root, width=62)
input2.place(x=330,y=130,height=30)

#button
button1 = ttk.Button(root, text="הצגת\nהטקסט",command=one)
button1.place(x=630,y=175)
button2 = ttk.Button(root, text="יישור\nלימין",command=two)
button2.place(x=530,y=175)
button3 = ttk.Button(root, text="היפוך\nלשמאל",command=three)
button3.place(x=430,y=175)
button4 = ttk.Button(root, text="ערבוב\nהמילה",command=four)
button4.place(x=330,y=175)
button5 = ttk.Button(root, text="העתק",command= copya)
button5.place(x=100,y=265)
button6 = ttk.Button(root, text="העתק",command=copyb)
button6.place(x=100,y=365)
button7 = ttk.Button(root, text="העתק",command=copyc)
button7.place(x=100,y=465)
button8 = ttk.Button(root, text="העתק",command=copyd)
button8.place(x=100,y=565)
button9 = tk.Button(root,width=10,text="שלח עכשיו",bg="white",border=0,cursor="hand2",fg="#57a1f8",command=send)
button9.place(x=40,y=65)

#frame
frame1 = tk.Frame(root,width=500,height=350,bg="white"
                  ,highlightbackground="black", highlightthickness=1)
frame1.place(x=200,y=250)

frame2 = tk.Frame(frame1,width=380,height=45,bg="white"
                  ,highlightbackground="black", highlightthickness=1)
frame2.place(x=20,y=0)

frame3 = tk.Frame(frame1,width=380,height=45,bg="white"
                  ,highlightbackground="black", highlightthickness=1)
frame3.place(x=20,y=100)

frame4 = tk.Frame(frame1,width=380,height=45,bg="white"
                  ,highlightbackground="black", highlightthickness=1)
frame4.place(x=20,y=200)

frame5 = tk.Frame(frame1,width=380,height=45,bg="white"
                  ,highlightbackground="black", highlightthickness=1)
frame5.place(x=20,y=300)

frame6 = tk.Frame(root,width=900,height=1,bg="white"
                  ,highlightbackground="black", highlightthickness=1)
frame6.place(x=0,y=230)

#frame labels

label3 = tk.Label(frame1, text="הצגת הטקסט",bg="white",font=("Ariel",12,"bold"))
label3.place(x=400,y=10)
label3 = tk.Label(frame1, text="יישור לימין",bg="white",font=("Ariel",12,"bold"))
label3.place(x=420,y=110)
label3 = tk.Label(frame1, text="היפוך לשמאל",bg="white",font=("Ariel",12,"bold"))
label3.place(x=405,y=210)
label3 = tk.Label(frame1, text="ערבוב המילה",bg="white",font=("Ariel",12,"bold"))
label3.place(x=405,y=310)

root.mainloop()
