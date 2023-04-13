from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Simple Calculator")

lbl1 = Label(window,text="Enter 1st number:")
lbl1.place(x=50,y=50)

lbl2 = Label(window,text="Enter 2nd number:")
lbl2.place(x=50,y=100)