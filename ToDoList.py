from tkinter import *

def add():
    new = entry.get()
    listbox.insert(END, new)
    entry.delete(0, END)
def delete_selected():
    sel = listbox.curselection()
    if sel:
        listbox.delete(sel[0])
        entry.delete(0, END)
def delete():
    listbox.delete(0,END)
    entry.delete(0, END)

window = Tk()
window.title("ToDo")
entry = Entry(window, font=('ink free', 15), bg='BLACK', fg='GREEN')
listbox = Listbox(window, font=('ink free', 15))
listbox.pack()
entry.pack()
button = Button(window, text="Add", command=  add, width=12, height=1)
button1 = Button(window, text="Delete Selected", command=  delete_selected, width=12, height=1)
button2 = Button(window, text="Delete", command=  delete, width=12, height=1)
button.pack(side=LEFT, pady=10, padx=10)
button1.pack(side=LEFT, pady=10, padx=10)
button2.pack(side=LEFT, pady=10, padx=10)
window.mainloop()