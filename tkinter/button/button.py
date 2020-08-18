import tkinter as tk

def hello_world():
    print("Hello World")
    # prints hello world in console

root = tk.Tk()
btn_say_hello = tk.Button(text="Hello",
    command = hello_world)
btn_say_hello.pack()
root.mainloop()

