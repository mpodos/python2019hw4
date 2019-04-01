#!/usr/bin/env python3
from tkinter import *

TKroot = Tk()
TKroot.title("Hello")

TKroot.columnconfigure(0, weight=1)
TKroot.rowconfigure(0, weight=1)
root = Frame(TKroot)
root.grid(sticky=E+W+S+N)

# масштабирование обеих колонок
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

def addButton():
    # заготовка под смену цвета
    def changeColor():
        pass
    colorButton = Button(root, text="Button", command=changeColor)
    colorLabel = Label(root, text="Label")
    tmp, row = root.size()
    # масштабирование добавленной строки
    root.rowconfigure(row+1, weight=1)
    colorButton.grid(row=row+1, column=0, sticky=E+W+S+N)
    colorLabel.grid(row=row+1, column=1, sticky=E+W+S+N)

def exitButton():
    root.quit()

Add = Button(root, text="Add", command=addButton)
Add.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Exit", command=exitButton)
Exit.grid(row=0, column=1, sticky=E+W+S+N)

TKroot.mainloop()
print("Done")
