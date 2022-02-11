import tkinter


def button_clicked():
    new_text = input.get()
    label.config(text=new_text)


window = tkinter.Tk()
window.title('My First GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
label = tkinter.Label(text='I Am a Label', font=('Arial', 24, 'bold'))
label.config(text='New Text')
label.grid(column=0, row=0)

# button
button1 = tkinter.Button(text='Click me', command=button_clicked)
button1.grid(column=1, row=1)

button2 = tkinter.Button(text='New Button')
button2.grid(column=2, row=0)

# entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
