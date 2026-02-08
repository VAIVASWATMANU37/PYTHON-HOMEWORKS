from tkinter import *
from tkinter import messagebox
from datetime import datetime
W = Tk()
W.title("AGE CALCULATOR")
W.geometry("500x500")
def calculate_age():
    dob_str = dob_entry.get()
    dob = datetime.strptime(dob_str, "%d/%m/%Y")
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    messagebox.showinfo("YOUR AGE IS", age)
label = Label(W, text="Enter your Date of Birth (DD/MM/YYYY):")
label.pack(pady=10)
dob_entry = Entry(W, width=30)
dob_entry.pack(pady=5)
calc_button = Button(W, text="Calculate Age", command=calculate_age)
calc_button.pack(pady=20)
W.mainloop()