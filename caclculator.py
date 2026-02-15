from tkinter import *
window = Tk()

window.geometry("300x400")
window.resizable(False, False)
disp = Entry(window, state='readonly', readonlybackground="white")
disp.grid(column=0, row=0, columnspan=4)
#row 1
seven = Button(window, text="7")
seven.grid(column=0,row=1, sticky='nesw')

eight = Button(window, text="8")
eight.grid(column=1,row=1, sticky='nesw')

nine = Button(window, text="9")
nine.grid(column=2,row=1, sticky='nesw')

divide = Button(window, text="÷")
divide.grid(column=3,row=1, sticky='nesw')

window.mainloop()