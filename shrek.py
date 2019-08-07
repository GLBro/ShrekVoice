import random,time
from playsound import playsound
import webbrowser
import speech_recognition as sr

#Reads the quotes
response = open("soundclips/shrekquotes", "r").readlines()

def handle_input(answer): 
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
       respond= playsound("soundclips/movie quotes (sound)/storyofshrek.mp3")
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
        respond = playsound ("soundclips/movie quotes (sound)/location.mp3") 
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
        respond = playsound("soundclips/movie quotes (sound)/scary.mp3") 
    elif "why" in answer or "look" in answer:
        respond = "i like my privacy"
    elif "how" in answer:
        respond = "hold the phone"
    elif "can" in answer or "we "in answer or"go"in answer:
        respond =  playsound("soundclips/movie quotes (sound)/adventure.mp3") 
    elif "best" in answer:
        respond =playsound("soundclips/movie quotes (sound)/repay.mp3") 
    elif "meme" in answer:
        respond =  playsound("soundclips/movie quotes (sound)/Shrek meme.mp3") 
    elif "cat" in answer or "puss in boots" in answer:
        respond = playsound("soundclips/movie quotes (sound)/kill.mp3")
    elif "Chrome" in answer:
        respond = webbrowser.open('http://google.co.kr', new=2)
    elif "fan" in answer or "page" in answer:
        respond=webbrowser.open("http://www.fanpop.com/clubs/shrek", new=2) 
    elif "youtube" in answer.lower() or "video" in answer:
        respond= webbrowser.open("https://www.youtube.com/watch?v=oCij5Kx5av0", new=2) 
    elif "news" in answer:
        respond= webbrowser.open("https://www.independent.co.uk/topic/Shrek", new=2) 
    elif "fortnite" in answer:
           respond= webbrowser.open("https://www.youtube.com/watch?v=C5MUSkfSL5c", new=2) 
    elif "git" in answer:
        respond= webbrowser.open("https://github.com/GLBro/ShrekVoice/issues ", new=2) 
         
    else: 
        respond = random.choice(response)
    print(respond)

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
            except sr.UnknownValueError:
                print('>>> unknown')
                continue
            print(answer)
            handle_input(answer)
except OSError:
    # We couldn't use the microphone as a source
    print('No Microphone, started in Text Mode')
    while True:
        answer = input('> ')
        time.sleep(random.randint(0,3))
        handle_input(answer)
