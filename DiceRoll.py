from tkinter import *
import random


def roll():
    def rolling():

            value = random.randint(1, 6)
            label.config(text=str(value))
            if value != 6:

                window.after(10, rolling)

            else:
                label.config(text=f"🎉 {value} 🎉")


    rolling()


window = Tk()
window.title('Dice Roll')
#window.geometry('500x500')
button = Button(window, text = 'Roll', command=roll, bg='black', fg='white', font=('ink free', 60, 'bold'))
button.pack(side=BOTTOM)
label = Label(window, text='', font=('ink free', 90))
label.pack()
#entry = Entry()
#entry.config(font=('ink free', 20))
#entry.pack()

window.mainloop()