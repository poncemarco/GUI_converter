from tkinter import *
# from playground import add
window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
# Label definition:
my_label = Label(text='I Am a Label', font=('Arial', 24, 'bold'))
# Set the label on the window
my_label['text']= 'New text'
my_label.config(text='New text')
# 3 maneras de colocar:
# pack, que pone una debajo de otra de manera lógica en el centro
# my_label.pack(side='left')  # another positions are: center, right, bottom, up
# place:
#my_label.place(x=100, y=0)  # Empiezan en el origen hacia el tercer cuadrante y las y positivas van hacia abajo
# Es dificil cuando tiene muchos widgets, solo puede estar un tipo de ellos en pantalla
# grid :
my_label.grid(column=0, row=0)
def button_clicked():
    print('I got it')
    new_text = input.get()
    my_label.config(text=new_text)



# Creating buttons
button_1 = Button(text='Click me', command=button_clicked)
#button.pack()
button_1.grid(column=1, row=1)
button_2 = Button(text='button')
button_2.grid(column=0, row=2)
# Does nothing


# Entry
input = Entry()
#input.pack()
input.grid(column=2, row= 3)
print(input.get())
window.mainloop()
