import tkinter as tk

def on_button_click():
    print("hello")

root = tk.Tk()

root.title("Calculator")
root.geometry("200x400")

label = tk.Label(root, text = "Calculator")

label.pack(pady=20)

button = tk.Button(
    root,
    text = "Submit",
    command = on_button_click
)

button.pack(pady=20)

root.mainloop()
