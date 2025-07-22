from tkinter import *
import random
def submit():
    num = entry.get()
    for i in range(int(num)):
        label = Label(window,text= random.randint(1,100), bg='#000FFF')
        label.pack()

window = Tk()
#window.geometry('480x480')
button = Button(window, text="Submit", command=submit)
button.pack(side = RIGHT)
window.title('Guesser')
entry = Entry()
entry.config(font=('ink free',25))
entry.config(bg='black')
entry.config(fg='#00FF00')
entry.pack()
window.mainloop()