from tkinter import *
#from PIL import Image, ImageTk

root = Tk()
root.title("Shrek chat box")
root.resizable(False, False)
shrekvoice =Entry()
shrekvoice.grid()

#func for text input
def buttonFunction():
    print("Shrek")

#bg image
shrekImage = PhotoImage(file="shrek is peng.png" )
shreklabel = Label(root, image=shrekImage)
shreklabel.grid(row=0)

#speech bubble
speechImage = PhotoImage(file="speechBubble.png" )
speechlabel = Label(root, image=speechImage)
speechlabel.place(x=0, y=0)

#response
respond = "shrek"
output = Label(text=respond) #prints value of 'respond' variable to the label!
output.place(x=80, y= 70)

#mic button
micButton=Button(root)
micImage=PhotoImage(file="mic.png")
micButton.config(image=micImage,width="100",height="100", bd=0,command=buttonFunction)
micButton.grid(row=13)

b = Button(root, text="enter!", command=buttonFunction) #text input button 
b.grid(row=1)

root.mainloop()

