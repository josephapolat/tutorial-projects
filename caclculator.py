from tkinter import *
from tkinter import ttk
window = Tk()

window.title("Calculator")

icon = PhotoImage(file="icon.png")

window.iconphoto(False, icon)

def on_button_click(value_to_insert):
    disp.insert(INSERT, value_to_insert)
def on_clear_button_click():
    disp.delete(0, END)
def on_delete_button_click():
    disp.delete(len(disp.get()) - 1)
def on_equal_button_click():
    result = eval(disp.get())  
    disp.delete(0, END)
    disp.insert(INSERT, result)
      
#Configure window and grid
window.geometry("300x400")
window.resizable(False, False)
disp = Entry(window, font=(48), readonlybackground="white")
disp.grid(column=0, columnspan=4,row=0, sticky="nesw")

#Setup columns to allow element fill
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

#Set up rows to allow for elemnt fill
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)


#Set up buttons
delete = Button(window, text="DEL", bg="#ECF2F5", relief=FLAT, command= on_delete_button_click)
delete.grid(column=3,row=1, sticky='nesw')

clear = Button(window, text="AC", bg="#ECF2F5", relief=FLAT, command= on_clear_button_click)
clear.grid(column=0,row=1, sticky='nesw')

leftParenth = Button(window, text="(", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("("))
leftParenth.grid(column=1,row=1, sticky='nesw')

rightParenth = Button(window, text=")", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click(")"))
rightParenth.grid(column=2,row=1, sticky='nesw')

exponent = Button(window, text="^", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("^"))
exponent.grid(column=0,row=2, sticky='nesw')

sqrRoot = Button(window, text="√", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("√"))
sqrRoot.grid(column=1,row=2, sticky='nesw')

percent = Button(window, text="%", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("%"))
percent.grid(column=2,row=2, sticky='nesw')

multiply = Button(window, text="*", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("*"))
multiply.grid(column=3,row=2, sticky='nesw')

seven = Button(window, text="7", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("7"))
seven.grid(column=0,row=3, sticky='nesw')

eight = Button(window, text="8", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("8"))
eight.grid(column=1,row=3, sticky='nesw')

nine = Button(window, text="9", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("9"))
nine.grid(column=2,row=3, sticky='nesw')

divide = Button(window, text="÷", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("/"))
divide.grid(column=3,row=3, sticky='nesw')

four = Button(window, text="4", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("4"))
four.grid(column=0,row=4, sticky='nesw')

five = Button(window, text="5", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("5"))
five.grid(column=1,row=4, sticky='nesw')

six = Button(window, text="6", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("6"))
six.grid(column=2,row=4, sticky='nesw')

minus = Button(window, text="-", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("-"))
minus.grid(column=3,row=4, sticky='nesw')

one = Button(window, text="1", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("1"))
one.grid(column=0,row=5, sticky='nesw')

two = Button(window, text="2", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("2"))
two.grid(column=1,row=5, sticky='nesw')

three = Button(window, text="3", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("3"))
three.grid(column=2,row=5, sticky='nesw')

plus = Button(window, text="+", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("+"))
plus.grid(column=3,row=5, sticky='nesw')

plusMinus = Button(window, text = "+/-", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("7"))
plusMinus.grid(column=0, row=6, sticky="nesw")

zero = Button(window, text = "0", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("0"))
zero.grid(column=1, row=6, sticky="nesw")

dot = Button(window, text = ".", bg="#ECF2F5", relief=FLAT, command=lambda: on_button_click("."))
dot.grid(column=2, row=6, sticky="nesw")

equals = Button(window, text = "=", bg="#ECF2F5", relief=FLAT, command= on_equal_button_click)
equals.grid(column=3, row=6, sticky="nesw")



window.mainloop()