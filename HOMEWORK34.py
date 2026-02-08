#NORMAL EDITONM (SOMEWHAT)
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
W=Tk()
W.title("Password Strength Checker")
W.config(bg="lightblue")
W.geometry("400x500")
L1=Label(W,bg="lightblue")
L1.place(x=100,y=20)
L2=Label(W,text="WELCOME TO THE PASSWORD STRENGTH CHECKER",font=("Arial",10,"bold"),bg="lightblue")
L2.place(relx=0.5,y=300,anchor="center")
def MESSAGE():
    MB=messagebox.askquestion("PASSWORD CHECKER","DO  YOU WANT TO CONTINUE?")
    if MB=="yes":
        TW()
B1=Button(W,text="START",font=("Arial",12,"bold"),bg="red",command=MESSAGE,fg="white",relief="raised")
B1.place(x=170,y=360)
def TW():
    T=Toplevel()
    T.title("STRENGTH ANALYZER")
    T.config(bg="lightgreen")
    T.geometry("500x450+50+50")   
    L3=Label(T,text="ENTER PASSWORD:",font=("Arial",14,"bold"),bg="lightgreen")
    L3.place(x=170,y=30)   
    E=Entry(T, font=("Arial", 12), show="*")
    E.place(x=160,y=70)
    L_len = Label(T, text="• Minimum 8 Characters", bg="lightgreen", font=("Arial", 10))
    L_num = Label(T, text="• Contains a Number", bg="lightgreen", font=("Arial", 10))
    L_up  = Label(T, text="• Contains Uppercase", bg="lightgreen", font=("Arial", 10))
    L_sp  = Label(T, text="• Contains Special Character", bg="lightgreen", font=("Arial", 10)) 
    L_len.place(x=160, y=180)
    L_num.place(x=160, y=210)
    L_up.place(x=160, y=240)
    L_sp.place(x=160, y=270)
    def CHECK():
        P = E.get()
        score = 0
        if len(P) >= 8:
            score += 1
            L_len.config(fg="darkgreen")
        else:
            L_len.config(fg="red")
        has_num = False
        has_upper = False
        has_special = False
        special_chars = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
        for char in P:
            if char.isdigit():
                has_num = True
            if char.isupper():
                has_upper = True
            if char in special_chars:
                has_special = True
        if has_num:
            score += 1
            L_num.config(fg="darkgreen")
        else:
            L_num.config(fg="red")
        if has_upper:
            score += 1
            L_up.config(fg="darkgreen")
        else:
            L_up.config(fg="red")
        if has_special:
            score += 1
            L_sp.config(fg="darkgreen")
        else:
            L_sp.config(fg="red")
        if score == 4:
            result = "STRONG"
        elif score >= 2:
            result = "MEDIUM"
        else:
            result = "WEAK"
        messagebox.showinfo("Result", f"Your Password is: {result}")
    B2=Button(T,text="CHECK STRENGTH",font=("Arial",12,"bold"),bg="brown",fg="white",command=CHECK)
    B2.place(x=170,y=120)
W.mainloop()