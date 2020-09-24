import tkinter as tk

def print_name():
    print(ent_name.get())
    # prints Foo Bar to console

root = tk.Tk()
lbl_name = tk.Label(text="Name")
ent_name = tk.Entry(width=20)
btn_print = tk.Button(text="Print name",
    command=print_name)
lbl_name.pack()
ent_name.pack()
btn_print.pack()
root.mainloop()


