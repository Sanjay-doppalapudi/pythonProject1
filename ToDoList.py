from tkinter import *

def add():
    new = entry.get()
    listbox.insert(END, new)
def delete_selected():
    sel = listbox.curselection()
    if sel:
        listbox.delete(sel[0])
def delete():
    listbox.delete(0,END)

window = Tk()
window.title("ToDo")
entry = Entry(window)
listbox = Listbox(window)
listbox.pack()
entry.pack()
button = Button(window, text="Add", command=  add)
button1 = Button(window, text="Delete Selected", command=  delete_selected)
button2 = Button(window, text="Delete", command=  delete)
button.pack()
button1.pack()
button2.pack()
window.mainloop()