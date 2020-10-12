from tkinter import *

root = Tk()

# the size can be changed
root.geometry("1250x700")

######## Functions

def printBot():
	label2.config(text='You Wrote :- '+e1.get("1.0",'end-1c'))

########  Main Code

label1 = Label(root, text="Enter Your Sentence", font=('Arial', 14, 'bold'))
label1.pack()

# e1 = Entry(root, width=40, border=3)
# e1.pack()

e1 = Text(root, width=60, height=10, border=3)
e1.pack()

b1 = Button(root, text="Click Me to Print!", bg="brown", fg="white", font=('Arial', 10), command=printBot)
b1.pack(pady=10)

label2 = Label(root, text="", font=('Roman', 14))
label2.pack(pady=(10,15))

label3 = Label(root, text="Positive %", font=('Arial', 14, 'bold'))
label3.pack(pady=(0,5))

mainloop()
