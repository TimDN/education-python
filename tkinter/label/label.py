import tkinter as tk

root = tk.Tk()
lbl_hello = tk.Label(text="Hello, Tkinter", bg="Blue",
    fg="White", justify="right", width=10, height=10,
    font=("Arial", 12, "bold "))
lbl_hello.pack()
root.mainloop()

