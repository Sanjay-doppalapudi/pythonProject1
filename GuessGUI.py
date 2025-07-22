from tkinter import *
def guess():

    name = "Sanjay"
    if name.upper() == entry.get().upper():
        label.config(text="You got that right", bg='#67ea7c')
    else:
        label.config(text="You got that wrong", bg='#e25343')


window = Tk()

entry = Entry(window)
entry.config(fg='GREEN', bg='#3e3f3e', font=('ink free', 35))
entry.pack()
button = Button(window, text='Guess', command = guess)
button.pack(pady=20, anchor='center')
label = Label(window, text='', font=('ink free', 35))
label.pack(side=BOTTOM)
window.mainloop()