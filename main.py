from tkinter import *


def miles_to_kilometers():
    num = int(A0.get())
    num *= 1.60934
    convertion.config(text=num)





window = Tk()
window.title("Converter program")
window.minsize(width=600, height=250)

# Text
miles = Label(text='Miles',font=('New Times Roman', 20))
miles.grid(column=3, row=0)

is_equal_to = Label(text='is equal to', font=('New Times Roman', 20))
is_equal_to.grid(column=1, row=1)

convertion = Label(text='0')
convertion.grid(column=2, row=1)



km = Label(text='Km', font=('New Times Roman', 20))
km.grid(column=3, row=1)



# Entry

A0 = Entry()
A0.grid(column=2, row=0)

# Button
calculate = Button(text='Calculate', font=('New Times Roman', 20), command=miles_to_kilometers)
calculate.grid(column=2, row=2)






window.mainloop()