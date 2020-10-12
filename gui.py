from tkinter import *

root = Tk()

# the size can be changed
root.geometry("1250x700")

# Here goes the main code

label1 = Label(root, text="Enter Your Sentence", font=('Arial', 14, 'bold'))
label1.pack()

# e1 = Entry(root, width=40, border=3)
# e1.pack()

e1 = Text(root, width=60, height=10, border=3)
e1.pack()

mainloop()
