import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}")


root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()
"""


quit_btn=ttk.Button(root,text='Quit',command=root.destroy)
quit_btn.pack(side='left',fill='x',expand=True)
"""

name_lbl = ttk.Label(root, text='Name: ')
name_lbl.pack(side='left', padx=(0, 10))
name_entr = ttk.Entry(root, width=15, textvariable=user_name)
name_entr.pack(side='left')
name_entr.focus()

button = ttk.Button(root, text='Greet', command=greet)
button.pack(side='left', fill='x', expand=True)
root.mainloop()

greet()
