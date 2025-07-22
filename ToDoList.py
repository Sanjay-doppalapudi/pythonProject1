from tkinter import *

def add():
    pass
def delete_selected():
    pass
def delete():
    pass

window = Tk()
window.title("ToDo")
entry = Entry(window)
entry.pack()
button = Button(window, text="Add", command=  add)
button1 = Button(window, text="Delete Selected", command=  delete_selected)
button2 = Button(window, text="Delete", command=  delete)
button.pack()
button1.pack()
button2.pack()
window.mainloop()