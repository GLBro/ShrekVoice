import random
import speech_recognition as sr

#Reads the quotes
response = open("soundclips/shrekquotes", "r").readlines()

def handle_input(answer): 
    #Any specific words mentioned trigger a response
    if "song" in answer:
        respond = "We will play a song"
    elif "swamp" in answer:
        rad = "Get out of my swamp!", "that would be my home"
        respond = random.choice(rad)
    elif "book" in answer:
        respond = "i read a book once"
    elif "annoying" in answer:
        rad = "could you be quiet just FOR 5 MINUTES!", "two things ok?Shut..up"
        respond = random.choice(rad)
    elif "story" in answer: 
        respond= "Once upon a time, there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon's keep, in the highest room of the tallest tower, for her true love, and true love's first kiss."
    elif "remind" in answer:
        respond = "its on my to do list"
    elif "princess" in answer or 'fiona' in answer:
        respond = "the princess will be up in the stairs in the highest room in the tallest tower"
    elif "ogre" in answer:
        respond = "ogres are like onions. onions have layers. ogres have layers"
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
        handle_input(answer)

