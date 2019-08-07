from tkinter import *
#from PIL import Image, ImageTk

root = Tk()
root.title("Shrek chat box")
root.resizable(False, False)

img=1
path="img"+str(img)+".png" 

#bg image
shrekImage = PhotoImage(file=path)
print(path)
shreklabel = Label(root, image=shrekImage)
shreklabel.grid(row=0)

#bg image change
def setImg():
    global img
    global path
    img+=1
    path="img"+str(img)+".png" 
    print(path)
    #shrekImage.file=path
    global shrekImage
    shrekImage = PhotoImage(file=path)
    shreklabel.configure(image=shrekImage)
    

#func for text input
def buttonFunction():
    global img
    global path
    setImg()



#speech bubble
speechImage = PhotoImage(file="speechBubble.png" )
speechlabel = Label(root, image=speechImage)
speechlabel.place(x=0, y=0)

#response
respond = "shrek"
output = Label(text=respond) #prints value of 'respond' variable to the label!
output.place(x=80, y= 45)
output.config(font=("Arial", 44),bg="#EDE6E6")

#input box
shrekvoice =Entry()
shrekvoice.grid()

#mic button
micButton=Button(root)
micImage=PhotoImage(file="mic.png")
micButton.config(image=micImage,width="100",height="100", bd=0,command=buttonFunction)
micButton.grid(row=13)

b = Button(root, text="enter!", command=buttonFunction) #text input button 
b.grid(row=2)


#shrekvoice.grid_remove() #hide element 

#setImg() #set bg image on run 
root.mainloop()




