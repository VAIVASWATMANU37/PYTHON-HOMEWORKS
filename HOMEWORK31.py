from tkinter import *
W = Tk()
W.title("Length Converter")
W.geometry("500x500")
def CONVERT(event):
        inches = float(EI.get())
        cm = inches * 2.54
        LR.config(text=f"{inches} inches = {cm} cm")
def EXIT():
    W.destroy()
LI = Label(W, text="Enter length in inches:", font=("Arial", 12))
LI.pack(pady=10)
EI = Entry(W, font=("Arial", 12))
EI.pack(pady=10)
B = Button(W, text="Convert", bg="BLACK", fg="GREEN", font=("Arial", 12))
B.pack(pady=10)
B.bind("<Button-1>", CONVERT)
L =  Label(W, text="RESULT:-", font=("Arial", 12), fg="BLUE")
L.pack(pady=10)
LR = Label(W, text="", font=("Arial", 12), fg="BLUE")
LR.pack(pady=10)
exit_button = Button(W, text="Exit", bg="BLUE", fg="RED", font=("Arial", 12), command=EXIT)
exit_button.pack(pady=10)
W.mainloop()