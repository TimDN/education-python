import tkinter as tk

windows = tk.Tk()
frm_a = tk.Frame()
lbl_a = tk.Label(master=frm_a, text="Im in frame A")
lbl_a.pack()

frm_b = tk.Frame()
lbl_b = tk.Label(master=frm_b, text="Im in frame B")
lbl_b.pack()

frm_b.pack()
frm_a.pack()
windows.mainloop()

