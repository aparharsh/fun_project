from tkinter import *

root = Tk()

# the size can be changed
root.geometry("1250x700")

######## Functions

def printBot():
	pass

########  Main Code

label1 = Label(root, text="Enter Your Sentence", font=('Arial', 14, 'bold'))
label1.pack()

# e1 = Entry(root, width=40, border=3)
# e1.pack()

e1 = Text(root, width=60, height=10, border=3)
e1.pack()

b1 = Button(root, text="Click Me to Print!", bg="brown", fg="white", font=('Arial', 10), command=printBot)
b1.pack(pady=10)

mainloop()
