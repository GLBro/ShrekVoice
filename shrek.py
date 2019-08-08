import random,time
from playsound import playsound
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import os

#Reads the quotes
response = open("soundclips/shrekquotes", "r").readlines()

#Sets ups text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 100) 
engine.setProperty('volume',1)
engine.say("Hello There")
engine.runAndWait()

'''shreksNo = random.randint(1,100)

def game(shreksNo):
    print("Guess my number!")    
    closeToShrek = shreksNo-7
    shreksNo_str = str(shreksNo)
    guess = input("Guess! ")
    if guess != shreksNo_str:
        print("My number is close to " + str(closeToShrek))
        game(shreksNo)
    else:
        print("you win ")'''

def handle_input(answer, listAnswer):
    respond = '' 
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

    elif "scary" in answer: 
        playsound("soundclips/movie quotes (sound)/scary.mp3") 
    elif "why" in answer or "look" in answer:
        respond = "i like my privacy"
    elif "how" in answer:
        respond = "hold the phone"
    elif "can" in answer or "we "in answer or"go"in answer:
        playsound("soundclips/movie quotes (sound)/adventure.mp3") 
    elif "best" in answer:
        playsound("soundclips/movie quotes (sound)/repay.mp3") 
    elif "meme" in answer:
        playsound("soundclips/movie quotes (sound)/Shrek meme.mp3") 
    elif "cat" in answer or "puss in boots" in answer:
        playsound("soundclips/movie quotes (sound)/kill.mp3")
    elif "Chrome" in answer:
        webbrowser.open('http://google.co.kr', new=2)
    elif "fan" in answer or "page" in answer:
          webbrowser.open("http://www.fanpop.com/clubs/shrek", new=2) 
    elif "youtube" in answer.lower() or "video" in answer:
        respond= webbrowser.open("https://www.youtube.com/watch?v=oCij5Kx5av0", new=2) 
    elif "news" in answer or "america" in answer:
        respond= webbrowser.open("https://www.youtube.com/watch?v=miDvziCKeI8", new=2) 
    elif "fortnite" in answer:
        respond= webbrowser.open("https://www.youtube.com/watch?v=C5MUSkfSL5c", new=2) 
    elif "git" in answer:
        respond= webbrowser.open("https://github.com/GLBro/ShrekVoice/issues", new=2) 
    elif "time" in answer:
         datetime.datetime.now()
    elif "day" in answer:
        respond= webbrowser.open("https://www.youtube.com/watch?v=A2c1f4FE8cY", new=2) 
    elif "music" in answer or "shreksophone" in answer or "instrument" in answer:
         respond= webbrowser.open("https://www.youtube.com/watch?v=_S7WEVLbQ-Y ", new=2) 
    elif "see" in answer or "eyes" in answer:
         respond= webbrowser.open("https://www.youtube.com/watch?v=QmTNoYJPhc0 ", new=2) 
    elif "donkey" in answer:
         respond= webbrowser.open("https://www.youtube.com/watch?v=rtUfvTzCDwE", new=2) 
    elif "dance" in answer:
          respond= webbrowser.open("https://www.youtube.com/watch?v=SF8fWC7xOJU", new=2)
    elif "French" in answer or "learn" in answer:
         respond= webbrowser.open("https://www.youtube.com/watch?v=QiLA-Igt1xg", new=2) 
    elif "stop" in answer:
          respond= webbrowser.open("https://www.youtube.com/watch?v=mseMvvgp86c", new=2) 
    elif "list" in answer:
        f= open("list.txt","w+")  
        print("you said: " + answer)
        f.write(answer)
        f.close()
        
        respond="your new folder is waiting " 

    elif "add" in answer:
        f=open("list.txt", "a+")
        f.write(answer)
        f.close()  

    elif "agenda" in answer:
        f= open("list.txt","r")
        if f.mode == 'r':
            contents =f.read()  
            respond = contents
    
    elif "delete"in answer:

            os.remove("list.txt")
            print("File Removed!")   

    elif "game" in answer:
       game(shreksNo)
            

    else: 
        random.choice(response)
    print(respond)
    engine.say(respond)
    engine.runAndWait()
# Try using a microphone, else fallback to reading from the console
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
                listAnswer = r.recognize_google(audio)
            except sr.UnknownValueError:
                print('>>> unknown')
                continue
            print(answer)
            handle_input(answer, listAnswer)
except OSError:
    # We couldn't use the microphone as a source
    print('No Microphone, started in Text Mode')
    while True:
        answer = input('> ')
        time.sleep(random.randint(0,3))
        handle_input(answer, listAnswer)
