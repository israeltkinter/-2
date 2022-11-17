import tkinter as tk
from tkinter import ttk
from tkinter import *
import os


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        #window

        self.title("חיבור בחיוג")
        self.geometry("339x425+500+200")
        self.resizable(False,False)
####################
        #labels
        self.img = PhotoImage(file="צילום מסך 2022-11-16 184407.png")
        label1 = ttk.Label(self,image=self.img)
        label1.place(x=0,y=0)
        label2 = ttk.Label(self, text=":שם משתמש")
        label2.place(x=260,y=160)
        label3 = ttk.Label(self, text=":סיסמה")
        label3.place(x=260, y=190)
        label4 = ttk.Label(self, text=":שמור שם משתמש וסיסמה אלה עבור השתמשים הבאים")
        label4.place(x=10, y=235)
        label5 = ttk.Label(self, text=":עבורי בלבד")
        label5.place(x=180, y=270)
        label6 = ttk.Label(self, text=":עבור כל אדם המשתמש במחשב זה")
        label6.place(x=60, y=290)
        label7 = ttk.Label(self, text=":חייג")
        label7.place(x=300,y=340)




##################################



        #buttons

        self.selected_opiton = tk.StringVar()
        self.storage_variable = tk.StringVar()

        check_button = ttk.Checkbutton(self,

                                       variable=self.selected_opiton,onvalue="On",offvalue="Off",
                                       command=self.check


                                       )

        check_button.place(x=300,y=235)

        self.option_one = ttk.Radiobutton(

            variable=self.storage_variable,
            value="First option"
        )

        self.option_tow = ttk.Radiobutton(

            variable=self.storage_variable,
            value="Second option"
        )



        self.option_one.place(x=250,y=270)
        self.option_one["state"] = "disabled"
        self.option_tow.place(x=250,y=290)

        self.option_tow["state"] = "disabled"

        button1 = ttk.Button(self,text="חייג",command=self.callcall)
        button2 = ttk.Button(self, text="ביטול",command=self.destroy)
        button3 = ttk.Button(self, text="מאפיינים")
        button4 = ttk.Button(self, text="עזרה",command=self.opening)
        button1.place(x=250,y=390)
        button2.place(x=170, y=390)
        button3.place(x=90, y=390)
        button4.place(x=10, y=390)
###############################################

        self.com_box = ttk.Combobox(width=35)
        self.com_box.place(x=30,y=340)
        self.com_box["values"] = ("99#*")
        self.com_box["state"] = "readonly"


        entry1 = ttk.Entry(self, width=38)
        entry1.place(x=10,y=160)
        entry2 = ttk.Entry(self, width=38)
        entry2.place(x=10, y=190)

        frame1 = tk.Frame(self, width=315,height=1,highlightbackground="black",highlightthickness=1)
        frame1.place(x=10,y=225)
        frame2 = tk.Frame(self, width=315, height=1, highlightbackground="black", highlightthickness=1)
        frame2.place(x=10, y=320)
        frame3 = tk.Frame(self, width=315, height=1, highlightbackground="black", highlightthickness=1)
        frame3.place(x=10, y=380)

    def check(self):
        self.printed = self.selected_opiton.get()

        if self.printed == "On":
            self.option_one["state"] = "normal"
            self.option_tow["state"] = "normal"
        elif self.printed == "Off":
             self.option_one["state"] = "disabled"
             self.option_tow["state"] = "disabled"

    def opening(self):
        os.system("start winhlp32.exe")

    def callcall(self):
        new = Toplevel(self)
        new.geometry('339x200+500+300')
        new.title("מתחבר לרשת")
        new.configure(bg="white")
        new.resizable(False,False)


        label1 = tk.Label(new,text="...מתחבר אל חיבור בחיוג",bg="white")
        label1.place(x=150,y=50)
        label2 = tk.Label(new, text="...המתן בזמן שהמערכת מבצעת התחברות לרשת", bg="white")
        label2.place(x=27, y=80)
        os.system("rasdial conn")
        label2 = tk.Label(new, text="!!!אתה מחובר", bg="white")
        label2.place(x=205, y=110)

        button1 = ttk.Button(new, text="התנתק",command=self.callup)
        button1.place(x=120,y=150)

        new.mainloop()


    def callup(self):
        os.system("rasdial/d")

root = Window()

root.mainloop()
