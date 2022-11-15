from tkinter import *
from tkinter import messagebox
import ast
import time
from tkinter import ttk
import os.path


root = Tk()
root.title("התחברות")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)



def signin():
    username = user.get()
    password = code.get()

    file=open('datasheet.dll','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    if username in r.keys() and password==r[username]:
        root.destroy()
        import system
    else:
        messagebox.showerror("לא חוקי","שם משתמש או סיסמה לא חוקיים")


def signup_command():
    window = Toplevel(root)
    window.title("הרשמה")
    window.geometry("925x500+300+200")
    window.resizable(False,False)
    window.configure(bg="#fff")


    def signup():
        username = user.get()
        password = code.get()
        confrom_password = confrom_code.get()

        if password == confrom_password and username != "שם משתמש" and username != "":
            if len(password)>4:
                try:
                    file=open('datasheet.dll','r+')
                    d=file.read()
                    r=ast.literal_eval(d)
                    dict2 = {username:password}
                    r.update(dict2)
                    file.truncate()
                    file.close()

                    file=open('datasheet.dll','w')
                    w=file.write(str(r))

                    messagebox.showinfo('הרשמה','נרשמת בהצלחה')
                except:
                    file=open('datasheet.dll','w')
                    pp=str({'Username':'password'})
                    file.write(pp)
                    file.close()

                
            elif len(password)<5:
                messagebox.showerror("לא חוקי", "סיסמה מידי קצרה")
        else:
            messagebox.showerror("לא חוקי", "ודא כי מלאת את כל התיבות נכון")

    def sign():
        window.destroy()

    img = PhotoImage(file="login (1).png")
    Label(window, image=img, border=0, bg="white").place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=480, y=50)

    heading = Label(frame, text="הרשמה", fg="#57a1f8", bg="white", font=("Microsoft Yhaei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    ########--------------------------------------------------------------------------------------------
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        if user.get() == '':
            user.insert(0, "שם משתמש")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Ariel", 11))
    user.place(x=30, y=80)
    user.insert(0, "שם משתמש")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    #########--------------------------------------------------------
    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        if code.get() == '':
            code.insert(0, "סיסמה")

    code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Ariel", 11))
    code.place(x=30, y=150)
    code.insert(0, "סיסמה")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    ################--------------------------------------------------
    def on_enter(e):
        confrom_code.delete(0, "end")

    def on_leave(e):
        if confrom_code.get() == '':
            confrom_code.insert(0, "זיהוי סיסמה")

    confrom_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yhaei UI Light", 11))
    confrom_code.place(x=30, y=220)
    confrom_code.insert(0, "זיהוי סיסמה")
    confrom_code.bind("<FocusIn>", on_enter)
    confrom_code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)
    ##########----------------------------------------------------------------------------------------------------

    Button(frame, width=39, pady=7, text="הרשמה", bg="#57a1f8", fg="white", border=0,command=signup).place(x=35, y=280)
    label = Label(frame, text="חשבון כבר לך יש?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=160, y=340)
    signin = Button(frame, width=6, text="התחבר", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign)
    signin.place(x=90, y=340)

    window.mainloop()

img = PhotoImage(file="login.gif")
Label(root,image=img,bg="white").place(x=50,y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text="התחברות", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100,y=5)

#########################-----------------------------------------------------------------------------------------

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, "שם משתמש")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Ariel", 11))
user.place(x=30,y=80)
user.insert(0,"שם משתמש")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
############################----------------------------------------------------------------------------------------

def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name=code.get()
    if name == '':
        code.insert(0, "סיסמה")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Ariel", 11))
code.place(x=30,y=150)
code.insert(0,"סיסמה")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
####################################################################

Button(frame,width=39,pady=7,text="התחברות",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="חשבון לך אין?",fg="black",bg="white",font=("Microsoft YaHei UI Light", 9))
label.place(x=140,y=270)
label = Label(frame,text="בעיות לך יש?",fg="black",bg="white",font=("Microsoft YaHei UI Light", 9))
label.place(x=140,y=300)

sign_up = Button(frame,width=6,text="הירשם",bg="white",border=0,cursor="hand2",fg="#57a1f8",command=signup_command)
sign_up.place(x=75,y=270)

def problem():
    root1 = Toplevel(root)
    root1.geometry("925x500+300+200")
    root1.title("פותר בעיות")
    root1.resizable(False, False)
    root1.configure(bg='white')

    label = Label(root1, text="     פתרון בעיות\nבהתחברות למערכת", font=("Ariel", 20, "bold"),bg="white")
    label.place(x=350, y=50)

    my_progres = ttk.Progressbar(root1, orient="horizontal",
                                 length=350, mode="determinate")
    my_progres.place(x=290, y=130)

    def step():
        # my_progres["value"] += 20
        # my_progres.start(10)
        #my_label.config(text=my_progres["value"])
        for x in range(5):
            my_progres["value"] += 20
            root.update_idletasks()
            time.sleep(0.5)
        my_progres.stop()
        printed = StringVar()
        printed2 = StringVar()
        printed3 = StringVar()
        file_exists = os.path.exists('datasheet.dll')
        if file_exists == True:
            printed.set("כן")
        elif file_exists == False:
            printed.set("לא")

        label1 = Label(root1, textvariable=printed,font=("Ariel",20, "bold"),fg="red",bg="white")
        label1.place(x=370, y=200)
        if printed.get() == "כן":
            label1.configure(fg="blue")
        elif printed.get() == "לא":
            label1.configure(fg="red")
        label2 = Label(root1, text="א, קובץ רישום קיים",font=("Ariel",20),bg="white")
        label2.place(x=420,y=200)
        label2 = Label(root1, text="ב, משתמש רשום במערכת", font=("Ariel", 20),bg="white")
        label2.place(x=420, y=230)
        label3 = Label(root1, textvariable=printed2, font=("Ariel", 20, "bold"),bg="white")
        label3.place(x=370, y=230)
        label4 = Label(root1, text="ג, סיסמה חוקית", font=("Ariel", 20),bg="white")
        label4.place(x=420, y=260)
        label5 = Label(root1, textvariable=printed3, font=("Ariel", 20, "bold"),bg="white")
        label5.place(x=370, y=260)
        label6 = Label(root1,text="בעיה א מלא מחדש פרטי הרשמה ולחץ פעמיים על כפתור ההרשמה",font=("Ariel",12),bg="white")
        label7 = Label(root1,text="בעיה ב הירשם למערכת",font=("Ariel",12),bg="white")
        label8 = Label(root1,text="בעיה ג הסיסמה שרשמת לא חוקית מלא סיסמה בת 5 ספרות לפחות",font=("Ariel",12),bg="white")
        label6.place(x=290,y=350)
        label7.place(x=550,y=400)
        label8.place(x=290,y=450)

        username = user.get()
        password = code.get()

        file1 = open("datasheet.dll", "r")
        d = file1.read()
        r = ast.literal_eval(d)

        if username in r.keys() and password == r[username]:
            printed2.set("כן")
        else:
            printed2.set("לא")
        file1.close()

        if len(password)<5:
            printed3.set("לא")
        else:
            printed3.set("כן")

        if printed2.get() == "כן":
            label3.configure(fg="blue")
        elif printed2.get() == "לא":
            label3.configure(fg="red")
        if printed3.get() == "כן":
            label5.configure(fg="blue")
        elif printed3.get() == "לא":
            label5.configure(fg="red")

    my_button = ttk.Button(root1, text="התחל", command=step)
    my_button.place(x=550, y=160)

    my_button2 = ttk.Button(root1, text="ביטול", command=root1.destroy)
    my_button2.place(x=300, y=160)

    my_label = ttk.Label(root1, text="")
    my_label.place(x=120, y=20)

    root1.mainloop()
sign_up = Button(frame,width=8,text="פתור בעיות",bg="white",border=0,cursor="hand2",fg="#57a1f8",command=problem)
sign_up.place(x=60,y=300)

root.mainloop()
