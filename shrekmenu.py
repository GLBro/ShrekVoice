from tkinter import *

root = Tk()
root.title("Shrek chat box")
root.geometry('300x300')
inputText= Entry().grid(row=8)
outputText= Entry().grid(row=10)



photo = PhotoImage(file="shrek is peng.png")
label = Label(root, image=photo)
label.grid(row=10)
def buttonFunction():
    print("Shrek")

b = Button(root, text="enter!", command=buttonFunction)
b.grid(row=1)

root.mainloop()

