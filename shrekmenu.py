from tkinter import *
#from PIL import Image, ImageTk

import random,time
from playsound import playsound
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import os

#--------------UI-----------------#
root = Tk()
root.title("Shrek chat box")
root.resizable(False, False)

#Reads the quotes
response = open("soundclips/shrekquotes", "r").readlines()

#Sets ups text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 110) 
engine.setProperty('volume',1)
engine.say("Hello There")
engine.runAndWait()

output = Label(text='') #prints value of 'respond' variable to the label!
output.place(x=80, y= 45)
output.config(font=("Arial", 44),bg="#EDE6E6")

respond = 'hi' 

def handle_input(answer):
    global output
    global respond
    #Any specific words mentioned trigger a response
    if "song" in answer:
        respond = "We will play a song,"
        playsound("soundclips/movie quotes (sound)/song.mp3")
    elif "swamp" in answer:
        rad = "Get out of my swamp!", "that would be my home"
        respond = random.choice(rad)
    elif "book" in answer:
        respond = "i read a book once"
    elif "annoying" in answer:
        rad = "could you be quiet just FOR 5 MINUTES!", "two things ok?Shut..up"
        respond = random.choice(rad)
    elif "story" in answer: 
       playsound("soundclips/movie quotes (sound)/storyofshrek.mp3")
       respond= "Once upon a time, there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon's keep, in the highest room of the tallest tower, for her true love, and true love's first kiss."
    elif "remind" in answer:
        respond = "its on my to do list"
    elif "princess" in answer or 'fiona' in answer or "where" in answer:
        respond = "the princess will be up in the stairs in the highest room in the tallest tower"
    elif "hate" in answer or "mean" in answer:
        respond = "well,thats not very nice."
    elif "ogre" in answer:
        respond = "ogres are like onions. onions have layers. ogres have layers"
    elif "will" in answer:
        respond = "yeah right before they burst into flame"
    elif "smart" in answer:
        respond = "well ER That explains a lot!"
    elif "sad" in answer:
        respond = "oh would you look at that!"
    elif "house" in answer:
        playsound ("soundclips/movie quotes (sound)/location.mp3") 
        respond = "sure it big enough...but look at the location!"
    elif "animal" in answer:
        respond = "its just a donkey"
    elif "loud" in answer:
        respond = "could you be quiet for 5 minutes FOR 5 MINUTES"
    elif "dinner" in answer:
        respond = "dead broad.. OFF THE TABLE!"
    elif "lonley" in answer or "name" in answer:
        respond = "well its no wonder you have no friends!"
    elif "Could" in answer:
        respond = "NO!"
    elif "do" in answer:
        respond = "Yes.NO!"
    elif "scary" in answer: 
        playsound("soundclips/movie quotes (sound)/scary.mp3") 
        respond = ''
    elif "why" in answer or "look" in answer:
        respond = "i like my privacy"
    elif "how" in answer:
        respond = "hold the phone"
    elif "can" in answer or "we "in answer or"go"in answer:
        playsound("soundclips/movie quotes (sound)/adventure.mp3")
        respond = ''
    elif "best" in answer:
        playsound("soundclips/movie quotes (sound)/repay.mp3")
        respond = '' 
    elif "meme" in answer:
        playsound("soundclips/movie quotes (sound)/Shrek meme.mp3")
        respond = '' 
    elif "cat" in answer or "puss in boots" in answer:
        playsound("soundclips/movie quotes (sound)/kill.mp3")
        respond = ''
    elif "Chrome" in answer:
        webbrowser.open('http://google.co.kr', new=2)
        respond = ''
    elif "fan" in answer or "page" in answer:
        webbrowser.open("http://www.fanpop.com/clubs/shrek", new=2)
        respond = ''
    elif "youtube" in answer.lower() or "video" in answer:
        webbrowser.open("https://www.youtube.com/watch?v=oCij5Kx5av0", new=2)
        respond = '' 
    elif "news" in answer:
        webbrowser.open("https://www.independent.co.uk/topic/Shrek", new=2)
        respond = '' 
    elif "fortnite" in answer:
        webbrowser.open("https://www.youtube.com/watch?v=C5MUSkfSL5c", new=2)
        respond = '' 
    elif "git" in answer:
        webbrowser.open("https://github.com/GLBro/ShrekVoice/issues ", new=2)
        respond = '' 
    elif "time" in answer:
        respond= datetime.datetime.now()
    else: 
        respond = random.choice(response)
    respond = respond.rstrip()
    print(respond)
    output.destroy()
    output = Label(text=respond) #prints value of 'respond' variable to the label!
    output.place(x=75, y= 45)
    output.config(font=("Arial", 25),bg="#EDE6E6")
    root.update()
    # import pdb; pdb.set_trace()

    engine.say(respond)
    engine.runAndWait()
# Try using a microphone, else fallback to reading from the console



def activateMic():
    try:
        #Setup microphone
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0)

        with mic as source:
            # The microphone worked, set it up further
            r.dynamic_energy_threshold = False    
            print('>>> ambient noise')
            r.adjust_for_ambient_noise(source)

            #Takes the input in  gives an output
            while True:
                print('>>> listening')
                audio = r.listen(source)
                try:
                    print('>>> sending to google')
                    answer = r.recognize_google(audio)
                except sr.UnknownValueError:
                    print('>>> unknown')
                    continue
                print(answer)
                handle_input(answer)
    except OSError:
        # We couldn't use the microphone as a source
    #print('No Microphone, started in Text Mode')
        while True:
            answer = input('> ')
            time.sleep(random.randint(0,3))
            handle_input(answer)






img=1
path="img"+str(img)+".png" 

# #bg image
shrekImage = PhotoImage(file=path)
shreklabel = Label(root, image=shrekImage)
shreklabel.grid(row=0)

#bg image change
def setImg():
    global img
    global path
    img+=1
    path="img"+str(img)+".png" 
    #shrekImage.file=path
    global shrekImage
    #shrekImage = PhotoImage(file=path)
    shreklabel.configure(image=shrekImage)
    

#func for text input
def buttonFunction():
    global img
    global path
    #setImg()



#speech bubble
speechImage = PhotoImage(file="speechBubble.png" )
speechlabel = Label(root, image=speechImage)
speechlabel.place(x=0, y=0)

#response
output = Label(text=respond) #prints value of 'respond' variable to the label!
output.place(x=80, y= 45)
output.config(font=("Arial", 44),bg="#EDE6E6")

'''what you say to Shrek
userInput = Label(text=answer) 
userInput.place(x=80, y= 100)
userInput.config(font=("Arial", 44),bg="#EDE6E6")'''

#input box
shrekvoice =Entry()
shrekvoice.grid()

#mic button
micButton=Button(root)
micImage=PhotoImage(file="mic.png")
micButton.config(image=micImage,width="100",height="100", bd=0,command = activateMic)
micButton.grid(row=13)

def MicNotAvailable():
    answer = shrekvoice.get()
    time.sleep(random.randint(0,3))
    handle_input(answer)
b = Button(root, text="enter!", command=MicNotAvailable) #text input button 
b.grid(row=2)


#shrekvoice.grid_remove() #hide element 

#setImg() #set bg image on run 
root.mainloop()





