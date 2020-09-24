import tkinter as tk

root = tk.Tk()
tkvar = tk.StringVar(root)

# Dictionary with options
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = tk.OptionMenu(root, tkvar, *choices)
popupMenu.pack()

# on change dropdown value
def change_dropdown(*args):
    print(tkvar.get())

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()

